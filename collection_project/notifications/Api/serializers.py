from utils.sign import encode_id
from ..models import ReminderLog
from rest_framework import serializers
from rest_framework.exceptions import NotFound, ValidationError

class ReminderLogSerializer(serializers.ModelSerializer):
	id = serializers.SerializerMethodField()
	invoice = serializers.SerializerMethodField()

	class Meta:
		model = ReminderLog
		fields = '__all__'
		read_only_fields = ['created_at', 'update_at', 'invoice']

	def get_id(self, obj):
		return encode_id(obj.pk)
	
	def get_invoice(self, obj):
		return encode_id(obj.invoice_id)