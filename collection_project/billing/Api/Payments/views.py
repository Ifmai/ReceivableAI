from ...Models.PaymentsModel import Payment
from utils.sign import decode_id
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from .serializers import PaymentSerializer, PaymentEncodeSerializer

class PaymentCreateView(generics.CreateAPIView):
	queryset = Payment.objects.all()
	serializer_class = PaymentSerializer

class PaymentListView(generics.ListAPIView):
	queryset = Payment.objects.all()
	serializer_class = PaymentEncodeSerializer

class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Payment.objects.all()
	serializer_class = PaymentEncodeSerializer
	lookup_url_kwarg = 'encrypted_id'

	def get_object(self):
		enc_id = self.kwargs('encryypted_id')
		try:
			pk = decode_id(enc_id)
		except:
			NotFound('Payment Not Found')
		return get_object_or_404(Payment, pk=pk)