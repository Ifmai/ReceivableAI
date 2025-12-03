from ..models import Customer
from utils.sign import decode_id
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from .serializers import CustomerSerializer, CustomerEncodeSerializer

class CustomerCreateView(generics.CreateAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

class CustomerListView(generics.ListAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerEncodeSerializer

class CustomerRetrieveView(generics.RetrieveAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerEncodeSerializer
	lookup_url_kwarg = "encrypted_id"

	def get_object(self):
		enc_id = self.kwargs["encrypted_id"]
		try:
			pk = decode_id(enc_id)
		except:
			raise NotFound("Customer Not Found")
		return get_object_or_404(Customer, pk=pk)

class CustomerUpdateView(generics.UpdateAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
	lookup_url_kwarg = "encrypted_id"

	def get_object(self):
		enc_id = self.kwargs["encrypted_id"]
		try:
			pk = decode_id(enc_id)
		except:
			raise NotFound("Customer Not Found")
		return get_object_or_404(Customer, pk=pk)

class CustomerDeleteView(generics.DestroyAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
	lookup_url_kwarg = "encrypted_id"

	def get_object(self):
		enc_id = self.kwargs["encrypted_id"]
		try:
			pk = decode_id(enc_id)
		except:
			raise NotFound("Customer Not Found")
		return get_object_or_404(Customer, pk=pk)