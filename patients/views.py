from django.db.models import Sum
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from .models import Doctor, PatientProfile, ClinicHistory
from .forms import PatientsForm
# =================================================================
# Patients
# =================================================================

class PatientList(LoginRequiredMixin, ListView):
	template_name = "patient_list.html"
	model = PatientProfile
	paginate_by = 10

class PatientDetailView(LoginRequiredMixin, DetailView):
	template_name = "patient_detail.html"
	model = PatientProfile

class PatientNew(LoginRequiredMixin, CreateView):
	template_name = "patient_new.html"
	model = PatientProfile
	success_url = reverse_lazy('') #	add link
	form_class = PatientsForm

	def form_valid(self, form):
		messages.success(self.request, response_messages.SAVE_SUCCESSFULL)
		form.instance.created_by = self.request.user
		return super(PatientNew, self).form_valid(form)

class PatientEdit(LoginRequiredMixin, UpdateView): 
	template_name = "patient_edit.html"
	model = PatientProfile
	form_class = PatientsForm
	success_url = reverse_lazy('') #	add link

	def form_valid(self, form):
		messages.success(self.request, response_messages.UPDATE_SUCCESSFULL)
		form.instance.created_by = self.request.user
		return super(PatientEdit, self).form_valid(form)

class PatientDelete(LoginRequiredMixin, DeleteView):
    template_name = "patient_delete.html"
    model = PatientProfile
    success_url = reverse_lazy('')

    def delete(self, request, *args, **kwargs):
        messages.success(request, response_messages.DELETE_SUCCESSFULL)
        return super(PatientDelete, self).delete(request, *args, **kwargs)

def test_view(request):
	return render(request, 'patient_detail.html')
