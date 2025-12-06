from django.urls import path
from .Invoice.views import *
from .Payments.views import *

urlpatterns = [
	#Invoice Urls Start
	path("invoices/add/", InvoiceCreateView.as_view(), name='invoice_create'),
	path("invoices/list/", InvoiceListView.as_view(), name='invoice_list'),
	path("invoices/upcoming/", InvoiceUpcomingView.as_view(), name='invoice_upcoming'),
	path("invoices/overdue/", InvoiceOverDueView.as_view(), name='invoice_overdue'),
	path("invoices/detail/<str:encrypted_id>/", InvoiceDetailView.as_view(), name='invoice_detail'),
	#Invoice Urls End

	#Payment Urls Start	
	path("payments/add/", PaymentCreateView.as_view(), name='Payment_create'),
	path("payments/list/", PaymentListView.as_view(), name='Payment_list'),
	path("payments/detail/<str:encrypted_id>/", PaymentDetailView.as_view(), name='payment_detail'),
	#Payment Urls End


]
