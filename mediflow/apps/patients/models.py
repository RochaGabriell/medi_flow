from django.db import models
from django.utils.translation import gettext_lazy as _

from mediflow.apps.users.models import UserModel


class PatientModel(models.Model):

    user = models.OneToOneField(
        UserModel,
        on_delete=models.PROTECT,
        verbose_name=_('User'),
        blank=True,
        null=True,
    )
    cpf = models.CharField(_('CPF'), max_length=11, unique=True)
    name = models.CharField(_('Name'), max_length=255)
    birth_date = models.DateField(_('Birth Date'))
    gender = models.CharField(
        _('Gender'),
        max_length=1,
        choices=[
            ('M', _('Man')),
            ('F', _('Female')),
            ('O', _('Other'))
        ],
    )
    phone = models.CharField(_('Phone'), max_length=20)
    email = models.EmailField(
        _('Email'),
        max_length=255,
        unique=True,
        null=True,
    )
    address = models.TextField(_('Address'))
    medical_history = models.TextField(
        _('Medical History'),
        blank=True,
        null=True
    )
    observations = models.TextField(
        _('Observations'),
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        verbose_name = _('Patient')
        verbose_name_plural = _('Patients')

    def __str__(self):
        return self.name
