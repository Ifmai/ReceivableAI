from django.db import models


class Customer (models.Model):
	name = models.CharField(max_length=50, null=False)
	tax_number = models.CharField(max_length=100, null=False, unique=True)
	e_mail = models.EmailField(unique=True)
	phone = models.IntegerField(blank=True, unique=True)
	status = models.BooleanField()
	created_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)


	def __str__(self):
		return f'{self.name}'
	class Meta:
		db_table = 'customers_customer'

