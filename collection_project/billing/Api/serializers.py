from ..models import Invoice
from utils.sign import encode_id
from rest_framework import serializers

class InvoiceSerializer(serializers.ModelSerializer):
	customer = serializers.CharField(source='customer.name', read_only=True)
	class Meta:
		model = Invoice
		fields = '__all__'
		read_only_fields = ['id', 'created_at', 'update_at']


class InvoiceEncodeSerializer(serializers.ModelSerializer):
	id = serializers.SerializerMethodField()
	customer = serializers.CharField(source='customer.name', read_only=True)

	class Meta:
		model = Invoice
		exclude = ['created_at', 'updated_at']

	def get_id(self, obj):
		return encode_id(obj.pk)