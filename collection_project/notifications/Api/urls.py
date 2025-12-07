from django.urls import path
from .views import ReminderLogCreateView, ReminderLogGetView

urlpatterns = [
	path("invoices/<str:invoice_id>/reminders/", 
	  ReminderLogCreateView.as_view(), name='remider_create'),
	path("invoices/<str:invoice_id>/reminders/list/", 
	  ReminderLogGetView.as_view(), name='remider_get'),
]
