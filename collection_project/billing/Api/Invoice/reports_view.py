from decimal import Decimal
from django.db.models import Sum
from rest_framework import generics
from rest_framework.response import Response
from ...Models.InvoiceModel import Invoice, Status
from django.db.models import Sum, F, DecimalField, Count, Q


class InvoiceReportsSummary(generics.GenericAPIView):
    queryset = Invoice.objects.all()

    def aggregate_amounts_by_currency(self, qs):
        response = qs.values("currency").annotate(
            total_price_invoice=Sum("total_price") or Decimal(0),
            total_paid_amount=Sum("paid_amount") or Decimal(0),
            total_outstanding=F("total_price_invoice") - F("total_paid_amount"),
        )
        return response

    def build_amount_dict_by_currency(self, rows):
        result = {}
        for row in rows:
            cur = row["currency"]
            result[cur] = {
                "total_price_invoice": row["total_price_invoice"] or Decimal("0"),
                "total_paid_amount": row["total_paid_amount"] or Decimal("0"),
                "total_outstanding": row["total_outstanding"] or Decimal("0"),
            }
        return result

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
        amounts_qs = self.aggregate_amounts_by_currency(qs)
        amounts_by_currency = self.build_amount_dict_by_currency(amounts_qs)
        # ----- Önümüzdeki 7 gün  bazlı toplamlar -----
        upcoming_qs = self.get_queryset().reminder()
        upcoming_7_days_count = upcoming_qs.count()
        upcoming_amounts_qs = self.aggregate_amounts_by_currency(upcoming_qs)
        upcoming_by_currency = self.build_amount_dict_by_currency(upcoming_amounts_qs)
        # ------- Overdue Faturalar bazlı toplamlar -----
        upcoming_overdue_qs = upcoming_qs.filter(status=Status.OVERDUE)
        overdue_7_days_count = upcoming_overdue_qs.count()
        overdue_amounts_qs = self.aggregate_amounts_by_currency(upcoming_overdue_qs)
        overdue_by_currency = self.build_amount_dict_by_currency(overdue_amounts_qs)

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
