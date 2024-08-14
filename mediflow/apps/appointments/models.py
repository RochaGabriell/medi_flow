from django.db import models
from django.utils.translation import gettext_lazy as _

from mediflow.apps.patients.models import PatientModel
from mediflow.apps.users.models import DoctorModel


class AppointmentModel(models.Model):

    patient = models.ForeignKey(
        PatientModel,
        on_delete=models.PROTECT,
        related_name='appointments_patient',
        verbose_name=_('Patient'),
    )
    doctor = models.ForeignKey(
        DoctorModel,
        on_delete=models.PROTECT,
        related_name='appointments_doctor',
        verbose_name=_('Doctor'),
    )
    description = models.TextField()
    notes = models.TextField(_('Notes'), blank=True, null=True)
    appointment_date = models.DateField(_('Appointment Date'))
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        unique_together = ('doctor', 'appointment_date')
        unique_together = ('patient', 'appointment_date')

        verbose_name = _('Appointment')
        verbose_name_plural = _('Appointments')

    def __str__(self):
        return f'{self.patient} - {self.appointment_date}'
