from django.urls import path
from .views import (
    MedicalRecordListView,
    MedicalRecordDetailView,
    MedicalRecordCreateView,
    MedicalRecordUpdateView,
    MedicalRecordDeleteView
)

urlpatterns = [
    path(
        'prontuarios/<int:patient_id>/',
        MedicalRecordListView.as_view(),
        name='medical_record_list'
    ),
    path(
        'prontuario/<int:pk>/',
        MedicalRecordDetailView.as_view(),
        name='medical_record_detail'
    ),
    path(
        'prontuario/novo/',
        MedicalRecordCreateView.as_view(),
        name='medical_record_create'
    ),
    path(
        'prontuario/<int:pk>/editar/',
        MedicalRecordUpdateView.as_view(),
        name='medical_record_update'
    ),
    path(
        'prontuario/<int:pk>/excluir/',
        MedicalRecordDeleteView.as_view(),
        name='medical_record_delete'
    ),
]
