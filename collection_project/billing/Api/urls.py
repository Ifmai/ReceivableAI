from django.urls import path
from .Invoice.views import *
from .Payments.views import *

urlpatterns = [
	#Invoice Urls Start
	
	#Invoice Post
	path("invoice/add/", InvoiceCreateView.as_view(), name='invoice_create'),
	
	#Invoice Get
	path("invoice/list/", InvoiceListView.as_view(), name='invoice_list'),
	path("invoices/upcoming/", InvoiceUpcomingView.as_view(), name='invoice_list'),
	path("invoice/<str:encrypted_id>/", InvoiceRetrieveView.as_view(), name='invoice_retrieve'),

	#Invoice Update Delete 
	path("invoice/update/<str:encrypted_id>/", InvoiceUpdateView.as_view(), name='invoice_update'),
	path("invoice/delete/<str:encrypted_id>/", InvoiceDeleteView.as_view(), name='invoice_delete'),
	
	#Invoice Urls End

	#Payment Urls Start	

	#Payment Post
	path("payment/add/", PaymentCreateView.as_view(), name='Payment_create'),
	
	#Payment Get
	path("payment/list/", PaymentListView.as_view(), name='Payment_list'),
	path("payment/<str:encrypted_id>/", PaymentRetrieveView.as_view(), name='Payment_retrieve'),
	
	#Payment Update Delete
	path("payment/update/<str:encrypted_id>/", PaymentUpdateView.as_view(), name='Payment_update'),
	path("payment/delete/<str:encrypted_id>/", PaymentDeleteView.as_view(), name='Payment_delete'),

	#Payment Urls End
]
