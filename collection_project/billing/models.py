from django.db import models

class Currency(models.TextChoices):
	USD = "USD", "US Dollar"
	EUR = "EUR", "Euro"
	TL = "TL", "Turkis Lira"

class Status(models.TextChoices):
	PENDING = "PENDING", "PENDING"
	PAID = "PAID", "PAID"
	OVERDUE = "OVERDUE", "OVERDUE"
	CANCELLED = "CANCELLED", "CANCELLED"

class Invoice(models.Model):
	customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE, related_name='invoices')
	external_invoice_id = models.CharField(max_length=254, null=False, blank=False)
	source_system = models.CharField(max_length=50, null=False, blank=False, default='MANUAL')
	total_price = models.DecimalField(max_digits=15, null=False, blank=False, decimal_places=2)
	currency = models.CharField(
		max_length=3,
		choices=Currency.choices,
		default=Currency.TL
	)
	issue_date = models.DateField()
	due_date = models.DateField()
	status = models.CharField(
		max_length=9,
		choices=Status.choices,
		default=Status.PENDING
	)
	comment = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.external_invoice_id} {self.customer}'

	class Meta:
		ordering = [
        models.Case(
            models.When(status='OVERDUE', then=0),
            default=1
        ),
        'due_date'
    ]