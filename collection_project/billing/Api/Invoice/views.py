from utils.sign import decode_id
from .filters import InvoiceFilter
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework.filters import OrderingFilter
from rest_framework.exceptions import ValidationError
from ...Models.InvoiceModel import Invoice, InvoiceQuerySet
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import InvoiceSerializer, InvoiceEncodeSerializer


class InvoiceCreateView(generics.CreateAPIView):
	queryset = Invoice.objects.all()
	serializer_class = InvoiceSerializer

class InvoiceListView(generics.ListAPIView):
	queryset = Invoice.objects.all()
	serializer_class = InvoiceEncodeSerializer
	
	filter_backends = [DjangoFilterBackend, OrderingFilter]
	filterset_class = InvoiceFilter

class InvoiceUpcomingView(generics.ListAPIView):
	serializer_class = InvoiceEncodeSerializer

	def get_queryset(self):
		days = self.request.query_params.get('days', 7)
		try:
			days = int(days)
		except ValueError:
			raise ValidationError({"days": "Invalid params. Days only number."})
		
		if days < 0:
			raise ValidationError({"days": "Days cannot be negative."})
		elif days > 365:
			raise ValidationError({"days:": "Days cannot be big 365."})
		
		return Invoice.objects.upcoming(days=days)

class InvoiceOverDueView(generics.ListAPIView):
	serializer_class = InvoiceEncodeSerializer

	def get_queryset(self):
		min_days_overdue = self.request.query_params.get('days', 0)

		try:
			min_days_overdue = int(min_days_overdue)
		except ValueError:
			raise ValidationError({"days": "Invalid params. Days only number."})

		if min_days_overdue < 0:
			raise ValidationError({"Days": "Days cannot be negative."})
		if min_days_overdue > 365:
			raise ValidationError({"Days": "Days cannot be big 365."})
		
		return Invoice.objects.overdue(min_days_overdue=min_days_overdue)

class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Invoice.objects.all()
	serializer_class = InvoiceEncodeSerializer
	lookup_url_kwarg = "encrypted_id"

	def get_object(self):
		enc_id = self.kwargs['encrypted_id']
		try:
			pk = decode_id(enc_id)
		except:
			raise NotFound("Invoice Not Found")
		return get_object_or_404(Invoice, pk=pk)