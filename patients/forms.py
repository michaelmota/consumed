from django import forms
from django.utils import timezone
from django.utils.translation import ugettext as _
from consumed.settings import DATE_INPUT_FORMATS

from .models import PatientProfile

class PatientsForm(forms.ModelForm):
	date = forms.DateField(input_formats=DATE_INPUT_FORMATS)

	class Meta:
		model = PatientProfile
		fields = ['first_name', 'last_name', 'cedula', 'sex', 'age', 'datebirth', 'refered_by', 'insurance', 
				'address', 'phone_1', 'phone_2', 'cellphone', 'ocupation', 'workplace', 'position', 
				'work_phone', 'emergency_contact', 'emergency_phone_1', 'emergency_phone_2', 
				'emergency_cellphone',]
