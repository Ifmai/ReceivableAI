from django.db import models
from django.db.models import Sum
from datetime import date, timedelta
class Currency(models.TextChoices):
	USD = "USD", "US Dollar"
	EUR = "EUR", "Euro"
	TL = "TL", "Turkis Lira"

class Status(models.TextChoices):
	PENDING = "PENDING", "PENDING"
	PAID = "PAID", "PAID"
	OVERDUE = "OVERDUE", "OVERDUE"
	CANCELLED = "CANCELLED", "CANCELLED"


class InvoiceQuerySet(models.QuerySet):

	def upcoming(self, days=7):
		today = date.today()
		end_date = today + timedelta(days)

		return self.filter(
			status=Status.PENDING,
			due_date__gte=today,
			due_date__lte=end_date
		)
	
	def overdue(self, min_days_overdue=0):
		if min_days_overdue != 0:
			today = date.today()
			end_date = today - timedelta(min_days_overdue)

			return self.filter(
				status=Status.OVERDUE,
				due_date__gte=end_date,
				due_date__lte=today
			)
		else:
			return self.filter(status=Status.OVERDUE)

class Invoice(models.Model):
	customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE, related_name='invoices')
	external_invoice_id = models.CharField(max_length=254, null=False, blank=False)
	source_system = models.CharField(max_length=50, null=False, blank=False, default='MANUAL')
	total_price = models.DecimalField(max_digits=15, null=False, blank=False, decimal_places=2)
	paid_amount = models.DecimalField(max_digits=15, null=True, blank=True, decimal_places=2, default=0)
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

	objects = InvoiceQuerySet.as_manager()

	def __str__(self):
		return f'{self.external_invoice_id} {self.customer} {self.total_price}'

	#Service Layer yazılabilir ama bu kadar küçük bir proje için gerek yok.
	#Gerek ihtiyaç duyulur ise geçirilebilir.
	def recalculate_status(self):
		total_invocies = self.payments.aggregate(total=Sum('amount'))['total'] or 0
		self.paid_amount = total_invocies
		if total_invocies >= self.total_price:
			self.status = "PAID"
		elif date.today() > self.due_date:
			self.status = "OVERDUE"
		else:
			self.status = "PENDING"

		self.save(update_fields=['status', 'paid_amount'])

	class Meta:
		constraints = [
			models.UniqueConstraint(
				fields=['source_system', 'external_invoice_id'],
				name='source_external_unuqie'
			)
		]
		ordering = [
        models.Case(
            models.When(status='OVERDUE', then=0),
            default=1
        ),
        'due_date'
    ]