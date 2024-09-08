from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import MedicalRecordModel


class MedicalRecordListView(ListView):
    model = MedicalRecordModel
    template_name = 'medical_record_list.html'
    context_object_name = 'medical_records'

    def get_queryset(self):
        return MedicalRecordModel.objects.filter(patient_id=self.kwargs['patient_id']).order_by('-created_at')


class MedicalRecordDetailView(DetailView):
    model = MedicalRecordModel
    template_name = 'medical_record_detail.html'
    context_object_name = 'medical_record'


class MedicalRecordCreateView(CreateView):
    model = MedicalRecordModel
    fields = ['patient', 'doctor', 'diagnosis', 'prescription', 'documents']
    template_name = 'medical_record_form.html'
    success_url = reverse_lazy('patient_list')


class MedicalRecordUpdateView(UpdateView):
    model = MedicalRecordModel
    fields = ['diagnosis', 'prescription', 'documents']
    template_name = 'medical_record_form.html'
    success_url = reverse_lazy('patient_list')


class MedicalRecordDeleteView(DeleteView):
    model = MedicalRecordModel
    template_name = 'medical_record_confirm_delete.html'
    success_url = reverse_lazy('patient_list')
