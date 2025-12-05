from django.urls import path
from .Invoice.views import *
from .Payments.views import *

urlpatterns = [
	path("invoice/add/", InvoiceCreateView.as_view(), name='invoice_create'),
	path("invoice/list/", InvoiceListView.as_view(), name='invoice_list'),
	path("invoice/<str:encrypted_id>/", InvoiceRetrieveView.as_view(), name='invoice_retrieve'),
	path("invoice/update/<str:encrypted_id>/", InvoiceUpdateView.as_view(), name='invoice_update'),
	path("invoice/delete/<str:encrypted_id>/", InvoiceDeleteView.as_view(), name='invoice_delete'),

	path("payment/add/", PaymentCreateView.as_view(), name='Payment_create'),
	path("payment/list/", PaymentListView.as_view(), name='Payment_list'),
	path("payment/<str:encrypted_id>/", PaymentRetrieveView.as_view(), name='Payment_retrieve'),
	path("payment/update/<str:encrypted_id>/", PaymentUpdateView.as_view(), name='Payment_update'),
	path("payment/delete/<str:encrypted_id>/", PaymentDeleteView.as_view(), name='Payment_delete'),
]
