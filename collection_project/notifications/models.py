from django.db import models

class ChannelChoise(models.TextChoices):
	EMAIL = 'EMAIL', 'EMAIL'
	SMS = 'SMS', 'SMS'
	MANUAL = 'MANUAL', 'MANUAL'

class StatusChooise(models.TextChoices):
	SENT = 'SENT', 'SENT'
	FAILED = 'FAILED', 'FAILED'
	DRAFT = 'DRAFT', 'DRAFT'

class ReminderLog(models.Model):
	invoice = models.ForeignKey('billing.Invoice', on_delete=models.CASCADE, related_name='reminders')
	channel = models.CharField(
		max_length=6, 
		null=False, 
		blank=False, 
		choices=ChannelChoise.choices, 
		default=ChannelChoise.EMAIL
	)
	sent_at = models.DateTimeField()
	subject = models.CharField(max_length=100, blank=True, null=True)
	status = models.CharField(
		max_length=6,
		choices=StatusChooise.choices,
		default=StatusChooise.DRAFT
	)
	preview = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.invoice.source_system}:{self.invoice.external_invoice_id} -> {self.invoice.customer}'