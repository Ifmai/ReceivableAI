from ...Models.InvoiceModel import Invoice
from utils.sign import decode_id
from .filters import InvoiceFilter
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework.filters import OrderingFilter
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

class InvoiceRetrieveView(generics.RetrieveAPIView):
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
	
class InvoiceUpdateView(generics.UpdateAPIView):
	queryset = Invoice.objects.all()
	serializer_class = InvoiceSerializer
	lookup_url_kwarg = "encrypted_id"

	def get_object(self):
		enc_id = self.kwargs['encrypted_id']
		try:
			pk = decode_id(enc_id)
		except:
			raise NotFound("Invoice Not Found")
		return get_object_or_404(Invoice, pk=pk)
	
class InvoiceDeleteView(generics.DestroyAPIView):
	queryset = Invoice.objects.all()
	serializer_class = InvoiceSerializer
	lookup_url_kwarg = "encrypted_id"

	def get_object(self):
		enc_id = self.kwargs['encrypted_id']
		try:
			pk = decode_id(enc_id)
		except:
			raise NotFound("Invoice Not Found")
		return get_object_or_404(Invoice, pk=pk)