from utils.sign import decode_key
from rest_framework import permissions
from django.conf import settings
from rest_framework.exceptions import ValidationError

class N8nPermission(permissions.BasePermission):

	def has_permission(self, request, view):
		hashed_key = request.headers.get('X-INTEGRATION-TOKEN')
		try:
			encode = decode_key(hashed_key)
			print("encode:", encode)
			if encode != settings.N8N_MESSAGE:
				Exception("GG WP!")
		except:
			print("selam knaka")
			self.message = '<3 <3 <3 <3'
			return False
		return True