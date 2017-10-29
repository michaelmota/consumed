from django.db.models import Sum
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, CreateView, DeleteView, UpdateView
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from .models import Doctor, PatientProfile, ClinicHistory

# =================================================================
# Patients
# =================================================================

class PatientList(LoginRequiredMixin, ListView):
	template_name = "patient_list.html"
	model = PatientProfile
	paginate_by = 10

class PatientNew(LoginRequiredMixin, CreateView):
	template_name = "patient_new.html"
	model = PatientProfile
	fields = ['full_name', 'cedula', 'sex', 'datebirth', 'refered_by', 'insurance', 
				'address', 'phone_1', 'phone_2', 'cellphone', 'ocupation', 'workplace', 'position', 
				'work_phone', 'emergency_contact', 'emergency_phone_1', 'emergency_phone_2', 
				'emergency_cellphone',]
	success_url = reverse_lazy('') #	add link

	def form_valid(self, form):
		messages.success(self.request, response_messages.SAVE_SUCCESSFULL)
		form.instance.created_by = self.request.user
		return super(PatientNew, self).form_valid(form)

class PatientEdit(LoginRequiredMixin, UpdateView): 
	template_name = "patient_edit.html"
	model = PatientProfile
	fields = ['full_name', 'cedula', 'sex', 'datebirth', 'refered_by', 'insurance', 
				'address', 'phone_1', 'phone_2', 'cellphone', 'ocupation', 'workplace', 'position', 
				'work_phone', 'emergency_contact', 'emergency_phone_1', 'emergency_phone_2', 
				'emergency_cellphone',]
	success_url = reverse_lazy('') #	add link

	def form_valid(self, form):
		messages.success(self.request, response_messages.UPDATE_SUCCESSFULL)
		form.instance.created_by = self.request.user
		return super(PatientNew, self).form_valid(form)

class PatientDelete(LoginRequiredMixin, DeleteView):
    template_name = "patient_delete.html"
    model = PatientProfile
    success_url = reverse_lazy('')

    def delete(self, request, *args, **kwargs):
        messages.success(request, response_messages.DELETE_SUCCESSFULL)
        return super(PatientDelete, self).delete(request, *args, **kwargs)

def test_view(request):
	return render(request, 'patient_detail.html')
