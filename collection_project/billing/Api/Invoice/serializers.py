from rest_framework import serializers
from ...Models.InvoiceModel import Invoice
from utils.sign import encode_id, decode_id
from rest_framework.exceptions import NotFound, ValidationError

class InvoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Invoice
		fields = '__all__'
		read_only_fields = ['id', 'created_at', 'update_at', 'paid_amount']

	#Django rest framework arayüzünden deneme yaparken bu kısımları yorum satırına alın.
	def to_internal_value(self, data):
			data = data.copy()

			if 'customer' in data:
				try:
					data['customer'] = decode_id(data['customer'])
				except:
					raise NotFound("Invoice Not Found")
				return super().to_internal_value(data)
			else:
				raise ValidationError({"error": "You need customer."})

class InvoiceEncodeSerializer(serializers.ModelSerializer):
	id = serializers.SerializerMethodField()
	customer = serializers.SerializerMethodField()

	class Meta:
		model = Invoice
		exclude = ['created_at', 'updated_at']

	def get_id(self, obj):
		return encode_id(obj.pk)
	
	def get_customer(self, obj):
		return encode_id(obj.customer_id)