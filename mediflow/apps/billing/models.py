from django.db import models
from django.utils.translation import gettext_lazy as _

from mediflow.apps.patients.models import PatientModel
from mediflow.apps.appointments.models import AppointmentModel
from mediflow.apps.inventory.models import InventoryModel


class BillingModel(models.Model):

    patient = models.ForeignKey(
        PatientModel,
        on_delete=models.CASCADE,
        related_name='billings_patient',
        verbose_name=_('Patient')
    )
    appointment = models.ForeignKey(
        AppointmentModel,
        on_delete=models.CASCADE,
        related_name='billings_appointment',
        verbose_name=_('Appointment')
    )
    amount = models.DecimalField(_('Amount'), max_digits=10, decimal_places=2)
    payment_status = models.CharField(
        max_length=20,
        choices=[
            ('pending', _('Pending')),
            ('paid', _('Paid')),
        ]
    )
    payment_date = models.DateTimeField(
        _('Payment Date'),
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        verbose_name = _('Billing')
        verbose_name_plural = _('Billings')

    def __str__(self):
        return f'{self.patient} - {self.date}'


class PaymentModel(models.Model):

    invoice = models.ForeignKey(
        BillingModel,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name=_('Invoice')
    )
    payment_method = models.CharField(
        max_length=20,
        choices=[
            ('cash', _('Cash')),
            ('card', _('Card')),
            ('online', _('Online')),
        ]
    )
    payment_date = models.DateTimeField(_('Payment Date'), auto_now_add=True)
    amount = models.DecimalField(_('Amount'), max_digits=10, decimal_places=2)
