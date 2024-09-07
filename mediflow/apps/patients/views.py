from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

from .models import PatientModel
from .forms import PatientForm


class PatientListView(ListView):
    model = PatientModel
    template_name = 'patient_list.html'


class PatientView(DetailView):
    model = PatientModel
    template_name = 'patient_detail.html'


class PatientCreateView(CreateView):
    model = PatientModel
    form_class = PatientForm
    template_name = 'patient_form.html'
    success_url = reverse_lazy('patient_list')


class PatientUpdateView(UpdateView):
    model = PatientModel
    form_class = PatientForm
    template_name = 'patient_form.html'
    success_url = reverse_lazy('patient_list')


class PatientDeleteView(DeleteView):
    model = PatientModel
    template_name = 'patient_confirm_delete.html'
    success_url = reverse_lazy('patient_list')
