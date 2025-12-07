from utils.sign import decode_key
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

class N8nPermission(permissions.BasePermission):

	def has_permission(self, request, view):
		hashed_key = request.headers.get('X-INTEGRATION-TOKEN')
		try:
			encode = decode_key(hashed_key)
		except:
			return False
		return True