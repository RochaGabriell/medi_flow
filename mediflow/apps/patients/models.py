from django.db import models
from django.utils.translation import gettext_lazy as _

from mediflow.apps.users.models import UserModel


class PatientModel(models.Model):

    user = models.OneToOneField(
        UserModel,
        on_delete=models.PROTECT,
        verbose_name=_('Usuário'),
    )
    cpf = models.CharField(_('CPF'), max_length=11, unique=True)
    name = models.CharField(_('Nome'), max_length=255)
    birth_date = models.DateField(_('Data de Nascimento'))
    gender = models.CharField(
        _('Gender'),
        max_length=1,
        choices=[
            ('M', _('Masculino')),
            ('F', _('Feminino')),
            ('O', _('Outro')),
        ],
    )
    phone = models.CharField(_('Nº de Telefone'), max_length=20)
    email = models.EmailField(
        _('Email'),
        max_length=255,
        unique=True,
        null=True,
    )
    address = models.TextField(_('Endereço'))
    medical_history = models.TextField(
        _('Histórico Médico'),
        blank=True,
        null=True
    )
    observations = models.TextField(
        _('Observações'),
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        verbose_name = _('Paciente')
        verbose_name_plural = _('Pacientes')

    def __str__(self):
        return self.name
