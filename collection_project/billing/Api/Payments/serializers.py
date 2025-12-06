from rest_framework import serializers
from ...Models.PaymentsModel import Payment
from utils.sign import encode_id, decode_id
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import ValidationError

class PaymentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Payment
		fields = '__all__'
		read_only_fields = ['id', 'created_at', 'update_at']

	def to_internal_value(self, data):
		data = data.copy()

		if 'invoice' in data:
			try:
				data['invoice'] = decode_id(data['invoice'])
			except:
				raise NotFound("Invoice Not Found")
			return super().to_internal_value(data)
		else:
			raise ValidationError({"error": "You need invoice."})


class PaymentEncodeSerializer(serializers.ModelSerializer):
	id = serializers.SerializerMethodField()
	invoice = serializers.CharField(source='invoice.source_system', read_only=True)

	class Meta:
		model = Payment
		exclude = ['created_at', 'update_at']

	def get_id(self, obj):
		return encode_id(obj.pk)