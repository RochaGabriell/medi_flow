from django.db import models
from django.utils.translation import gettext_lazy as _

from mediflow.apps.patients.models import PatientModel
from mediflow.apps.users.models import DoctorModel


class MedicalRecordModel(models.Model):

    patient = models.ForeignKey(
        PatientModel,
        on_delete=models.CASCADE,
        related_name='medical_records',
        verbose_name=_('Patient')
    )
    doctor = models.ForeignKey(
        DoctorModel,
        on_delete=models.CASCADE,
        related_name='medical_records',
        verbose_name=_('Doctor')
    )
    diagnosis = models.TextField(_('Diagnosis'))
    prescription = models.TextField(_('Prescription'))
    documents = models.FileField(
        upload_to='medical_records/',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        verbose_name = _('Medical Record')
        verbose_name_plural = _('Medical Records')

    def __str__(self):
        return f'{self.patient} - {self.date}'
