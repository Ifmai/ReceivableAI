from django.db import models
from .InvoiceModel import Invoice


class Payment(models.Model):
	invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='payments')
	amount = models.DecimalField(max_digits=15, null=False, blank=False, decimal_places=2)
	payment_date = models.DateField(null=False, blank=False)
	method = models.CharField(max_length=50, null=False, blank=False)
	note = models.TextField(max_length=250, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.invoice}'
	
	#Service Layer yazılabilir ama bu kadar küçük bir proje için gerek yok.
	#Gerek ihtiyaç duyulur ise geçirilebilir.
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		self.invoice.recalculate_status()

	def delete(self, *args, **kwargs):
		invoice = self.invoice
		super().delete(*args, **kwargs)
		invoice.recalculate_status()