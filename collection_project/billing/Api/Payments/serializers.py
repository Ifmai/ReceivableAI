from ...Models.PaymentsModel import Payment
from utils.sign import encode_id
from rest_framework import serializers

class PaymentSerializer(serializers.ModelSerializer):
	invoice = serializers.CharField(source='invoice.source_system', read_only=True)
	class Meta:
		model = Payment
		fields = '__all__'
		read_only_fields = ['id', 'created_at', 'update_at']


class PaymentEncodeSerializer(serializers.ModelSerializer):
	id = serializers.SerializerMethodField()
	invoice = serializers.CharField(source='invoice.source_system', read_only=True)

	class Meta:
		model = Payment
		exclude = ['created_at', 'update_at']

	def get_id(self, obj):
		return encode_id(obj.pk)