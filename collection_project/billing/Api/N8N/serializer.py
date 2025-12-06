from utils.sign import encode_id
from rest_framework import serializers
from ...Models.InvoiceModel import Invoice

class InvoicesReminderSerializer(serializers.ModelSerializer):
	id = serializers.SerializerMethodField()
	customer_name = serializers.CharField(source='customer.name', read_only=True)
	customer_email = serializers.CharField(source='customer.e_mail', read_only=True)

	class Meta:
		model = Invoice
		fields = [
			'id', 'external_invoice_id', 'customer_name', 
			'customer_email', 'total_price', 'currency',
			'due_date', 'status']
	
	def get_id(self, obj):
		return encode_id(obj.pk)