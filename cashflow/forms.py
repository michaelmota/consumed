from django import forms
from django.utils import timezone
from django.utils.translation import ugettext as _
from consumed.internationalization import DATE_INPUT_FORMATS

class TransactionForm(forms.ModelForm):
	date = forms.DateField(input_formats=DATE_INPUT_FORMATS)

	class Meta:
		model = Transaction
		fields = ['account', 'name', 'category', 'amount', 'date']
