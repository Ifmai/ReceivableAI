from ..models import Customer
from utils.sign import encode_id
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = '__all__'
		read_only_fields = ['id', 'created_at', 'updated_at']

class CustomerEncodeSerializer(serializers.ModelSerializer):
	id = serializers.SerializerMethodField()

	class Meta:
		model = Customer
		exclude = ['created_at', 'updated_at']

	def get_id(self, obj):
		return encode_id(obj.pk)