from django.contrib import admin
from .Models.InvoiceModel import Invoice
from .Models.PaymentsModel import Payment

admin.site.register(Invoice)
admin.site.register(Payment)