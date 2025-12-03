from django.urls import path
from .Api.view import *

urlpatterns = [
	path("add/", CustomerCreateView.as_view(), name="customer_add"),
	path("list/", CustomerListView.as_view(), name="customer_list"),
	path("<str:encrypted_id>/", CustomerRetrieveView.as_view(), name='customer_retrieve'),
	path("update/<str:encrypted_id>/", CustomerUpdateView.as_view(), name='customer_retrieve'),
	path("delete/<str:encrypted_id>/", CustomerDeleteView.as_view(), name="customer_delete"),
]
