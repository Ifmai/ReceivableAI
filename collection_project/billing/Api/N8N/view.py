from rest_framework import generics
from ...Models.InvoiceModel import Invoice
from .serializer import InvoicesReminderSerializer
from permission.n8n_permission import N8nPermission
from rest_framework.exceptions import ValidationError

class InvoiceReminderCandidatesView(generics.ListAPIView):
	serializer_class = InvoicesReminderSerializer
	permission_classes = [N8nPermission]

	def get_queryset(self):
		days = self.request.query_params.get('days', 7)
		try:
			days = int(days)
		except ValueError:
			raise ValidationError({"days": "Invalid params. Days only number."})
		
		if days < 0:
			raise ValidationError({"days": "Days cannot be negative."})
		elif days > 365:
			raise ValidationError({"days:": "Days cannot be big 365."})
		
		return Invoice.objects.reminder(reminder_days=days)