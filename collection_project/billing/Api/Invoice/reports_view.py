from decimal import Decimal
from utils.sign import decode_id
from django.db.models import Sum
from rest_framework import generics
from customers.models import Customer
from rest_framework.response import Response
from django.db.models import Sum, F, Count, Q
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from ...Models.InvoiceModel import Invoice, Status


def aggregate_amounts_by_currency(qs):
    response = qs.values("currency").annotate(
        total_price_invoice=Sum("total_price") or Decimal(0),
        total_paid_amount=Sum("paid_amount") or Decimal(0),
        total_outstanding=F("total_price_invoice") - F("total_paid_amount"),
    )
    return response

def build_amount_dict_by_currency(rows):
    result = {}
    for row in rows:
        cur = row["currency"]
        result[cur] = {
            "total_price_invoice": row["total_price_invoice"] or Decimal("0"),
            "total_paid_amount": row["total_paid_amount"] or Decimal("0"),
            "total_outstanding": row["total_outstanding"] or Decimal("0"),
        }
    return result


class InvoiceReportsSummary(generics.GenericAPIView):
    queryset = Invoice.objects.all()



    def get(self, request, *args, **kwargs):

        qs = self.get_queryset()
        # ----- Genel sayılar -----
        count = qs.aggregate(
            total_invoices=Count("id"),
            pending=Count("id", filter=Q(status=Status.PENDING)),
            paid=Count("id", filter=Q(status=Status.PAID)),
            overdue=Count("id", filter=Q(status=Status.OVERDUE)),
        )
        # ----- Currency bazlı toplamlar -----
        amounts_qs = aggregate_amounts_by_currency(qs)
        amounts_by_currency = build_amount_dict_by_currency(amounts_qs)
        # ----- Önümüzdeki 7 gün  bazlı toplamlar -----
        upcoming_qs = self.get_queryset().reminder()
        upcoming_7_days_count = upcoming_qs.count()
        upcoming_amounts_qs = aggregate_amounts_by_currency(upcoming_qs)
        upcoming_by_currency = build_amount_dict_by_currency(upcoming_amounts_qs)
        # ------- Overdue Faturalar bazlı toplamlar -----
        upcoming_overdue_qs = upcoming_qs.filter(status=Status.OVERDUE)
        overdue_7_days_count = upcoming_overdue_qs.count()
        overdue_amounts_qs = aggregate_amounts_by_currency(upcoming_overdue_qs)
        overdue_by_currency = build_amount_dict_by_currency(overdue_amounts_qs)

        data = {
            "counts": count,
            "amounts_by_currency": amounts_by_currency,
            "upcoming_7_days": {
                "invoice_count": upcoming_7_days_count,
                "amounts_by_currency": upcoming_by_currency,
            },
            "upcoming_7_days_overdue": {
                "invoice_count": overdue_7_days_count,
                "amounts_by_currency": overdue_by_currency,
            },
        }
        return Response(data)


class CustomerReportsSummary(generics.GenericAPIView):
    lookup_url_kwarg = 'customer_id'

    def get_queryset(self):
        customer_encode_id = self.kwargs['customer_id']
        try:
            customer_id = decode_id(customer_encode_id)
            find_customer = get_object_or_404(Customer, pk=customer_id)
        except:
            raise NotFound("Not Found Customer")
        qs = Invoice.objects.filter(customer=customer_id)
        return qs, find_customer
    
    def  get(self, request, *args, **kwargs):
        qs, customer = self.get_queryset()

        count = qs.aggregate(
            total_invoice=Count('id'),
            total_pending=Count('id', filter=Q(status=Status.PENDING)),
            total_paid=Count('id', filter=Q(status=Status.PAID)),
            total_overdue=Count('id', filter=Q(status=Status.OVERDUE))
        )

        amount_currency_qs = aggregate_amounts_by_currency(qs)
        amount_currency = build_amount_dict_by_currency(amount_currency_qs)
        top_5_quest = qs.upcoming(days=7).order_by('-due_date')[:5]
        
        return Response({
            "customer": customer.name,
            "counts": count,
            "amounts_by_currency": amount_currency,
            "up_coming_5_invoice": top_5_quest
        }) 
    
