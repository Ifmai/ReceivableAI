from utils.sign import decode_id
from ...Models.InvoiceModel import Invoice, Status
from django_filters import FilterSet, MultipleChoiceFilter, CharFilter, DateFromToRangeFilter

class InvoiceFilter(FilterSet):
	status = MultipleChoiceFilter(
		field_name='status',
		choices=Status.choices
	)

	customer = CharFilter(method='filter_customer')
	date = DateFromToRangeFilter(field_name='due_date')

	class Meta:
		model = Invoice
		fields = []
	
	def filter_customer(self, queryset, name, value):
		if not value:
			return queryset
		try:
			customer_id = decode_id(value=value)
		except:
			return queryset.none()
		return queryset.filter(customer_id=customer_id)