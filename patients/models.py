from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

from .constants import sex, ars_insurance

class Doctor(models.Model):
	"""App that will manage all the doctors on the center."""
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	cedula = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	cellphone = models.CharField(max_length=255)
	email = models.CharField(max_length=255)

	def __str__(self):
		return "%s %s" %(self.first_name, self.last_name)

class PatientProfile(models.Model):
	"""App that will manage the profile of a patient."""
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	cedula = models.CharField(max_length=255)
	sex = models.CharField(max_length=255, choices=sex)
	age = models.CharField(max_length=3)
	datebirth = models.DateField()
	refered_by = models.CharField(max_length=255)
	insurance = models.CharField(max_length=255, choices=ars_insurance)
	# Contact Info
	address = models.CharField(max_length=255, blank=True)
	phone_1 = models.CharField(max_length=255, blank=True)
	phone_2 = models.CharField(max_length=255, blank=True)
	cellphone = models.CharField(max_length=255, blank=True)
	# Work Information
	ocupation = models.CharField(max_length=255, blank=True)
	workplace = models.CharField(max_length=255, blank=True)
	position = models.CharField(max_length=255, blank=True)
	work_phone = models.CharField(max_length=255, blank=True)
	# Emergency Contact
	emergency_contact = models.CharField(max_length=255, blank=True)
	emergency_phone_1 = models.CharField(max_length=255, blank=True)
	emergency_phone_2 = models.CharField(max_length=255, blank=True)
	emergency_cellphone = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return '%s %s' %(self.first_name, self.last_name)

class ClinicHistory(models.Model):
	"""App that will manage all the clinic history of a patient."""
	patient = models.ForeignKey(PatientProfile)
	doctor = models.ForeignKey(Doctor)
	personal_history = models.TextField(max_length=500, blank=True)
	family_history = models.TextField(max_length=500, blank=True)
	current_illness = models.TextField(max_length=500, blank=True)
	symptoms = models.TextField(max_length=500, blank=True)
	rehab_diagnose = models.TextField(max_length=1000, blank=True)
	short_term_goals = models.TextField(max_length=1000, blank=True)
	long_term_goals = models.TextField(max_length=1000, blank=True)
	form_filled_by = models.CharField(max_length=255)

	def __str__(self):
		return str(self.patient)

class Therapy(models.Model):
	"""Manages the therapy's for each of the patients."""
	patient = models.ForeignKey(PatientProfile)
	doctor = models.ForeignKey(Doctor)
	date = models.DateField(help_text=_("Fecha de la Terapia"), verbose_name=_("Fecha"))
	insurance = models.CharField(max_length=155, choices=ars_insurance)
	physiotherapy = models.TextField(max_length=2000, blank=True)
	diagnosis = models.TextField(max_length=2000, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def get_absolute_url(self):
		return reverse('patient-view', kwargs={'pk': self.pk})

	def __str__(self):
		return str(self.patient)




