from django.urls import path, include
from .Invoice.views import *
from .Invoice.reports_view import InvoiceReportsSummary
from .Payments.views import *

urlpatterns = [
    # Invoice CRID Urls Start
    path("invoices/add/", InvoiceCreateView.as_view(), name="invoice_create"),
    path("invoices/list/", InvoiceListView.as_view(), name="invoice_list"),
    path("invoices/upcoming/", InvoiceUpcomingView.as_view(), name="invoice_upcoming"),
    path("invoices/overdue/", InvoiceOverDueView.as_view(), name="invoice_overdue"),
    path("invoices/detail/<str:encrypted_id>/", InvoiceDetailView.as_view(), name="invoice_detail"),
    path("invoices/reports/summary/", InvoiceReportsSummary.as_view(), name="invoice_summary"),
    # Invoice Urls End
    # Payment Urls Start
    path("payments/add/", PaymentCreateView.as_view(), name="Payment_create"),
    path("payments/list/", PaymentListView.as_view(), name="Payment_list"),
    path("payments/detail/<str:encrypted_id>/", PaymentDetailView.as_view(), name="payment_detail"),
    # Payment Urls End
    # Integration Urls (n8n vb. için) Start
    path("integrations/", include("billing.Api.N8N.urls")),
    # Integration Urls (n8n vb. için) End
]
