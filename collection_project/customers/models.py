from django.db import models


class Customer (models.Model):
	name = models.CharField(max_length=50, null=False)
	tax_number = models.CharField(max_length=100, null=False, unique=True)
	e_mail = models.EmailField(null=False)
	phone = models.DecimalField(blank=True, max_digits=11, decimal_places=0)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return f'{self.name}'
	class Meta:
		db_table = 'customers_customer'
		ordering = ['name']
