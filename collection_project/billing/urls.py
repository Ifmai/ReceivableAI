from django.urls import path
from .Api.InvoiceView import *

urlpatterns = [
	path("add/", InvoiceCreateView.as_view(), name='invoice_create'),
	path("list/", InvoiceListView.as_view(), name='invoice_list'),
	path("<str:encrypted_id>/", InvoiceRetrieveView.as_view(), name='invoice_retrieve'),
	path("update/<str:encrypted_id>/", InvoiceUpdateView.as_view(), name='invoice_update'),
	path("delete/<str:encrypted_id>/", InvoiceDeleteView.as_view(), name='invoice_delete'),
]
