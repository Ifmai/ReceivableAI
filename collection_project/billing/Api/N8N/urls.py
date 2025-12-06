from django.urls import path
from .view import InvoiceReminderCandidatesView

urlpatterns = [
	path(
        "invoices/reminder-candidates/",
        InvoiceReminderCandidatesView.as_view(),
        name="n8n_invoice_reminder_candidates",
    ),
]
