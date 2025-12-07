from ..models import ReminderLog
from utils.sign import decode_id
from rest_framework import generics
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from .serializers import ReminderLogSerializer
from billing.Models.InvoiceModel import Invoice

def get_invoice(encrypted_id=''):
	try:
		invoice_id = decode_id(encrypted_id)
		print("invoice_id:", invoice_id)
	except:
		raise NotFound("Invoice Not Found")
	return get_object_or_404(Invoice, pk=invoice_id)


class ReminderLogCreateView(generics.CreateAPIView):
	queryset = ReminderLog.objects.all()
	serializer_class = ReminderLogSerializer
	
	def perform_create(self, serializer):
		invoice = get_invoice(self.kwargs['invoice_id'])
		reminder = serializer.save(invoice=invoice)
		invoice.save(update_fields=['updated_at'])


class ReminderLogGetView(generics.ListAPIView):
	serializer_class = ReminderLogSerializer

	def get_queryset(self):
		invoice = get_invoice(self.kwargs['invoice_id'])
		queryset = ReminderLog.objects.filter(invoice=invoice).order_by('-sent_at')
		return queryset