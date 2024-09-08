from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class UserModel(AbstractUser):

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('receptionist', 'Receptionist'),
        ('patient', 'Patient'),
    ]
    role = models.CharField(
        _('Função'),
        max_length=20,
        choices=ROLE_CHOICES,
        default='patient'
    )

    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')

    def __str__(self):
        return self.username


class DoctorModel(models.Model):

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
    )
    crm = models.CharField(_('CRM'), max_length=20)
    especiality = models.CharField(_('Especialidade'), max_length=255)

    class Meta:
        verbose_name = _('Médico')
        verbose_name_plural = _('Médicos')

    def __str__(self):
        return f'{self.user.username} - {self.especiality}'


class DoctorAvailabilityModel(models.Model):
    doctor = models.ForeignKey(
        DoctorModel,
        on_delete=models.CASCADE,
        related_name='availabilities',
        verbose_name=_('Médico')
    )
    day_of_week = models.IntegerField(
        _('Dia da Semana'),
        choices=[
            (0, _('Segunda-feira')),
            (1, _('Terça-feira')),
            (2, _('Quarta-feira')),
            (3, _('Quinta-feira')),
            (4, _('Sexta-feira')),
            (5, _('Sábado')),
            (6, _('Domingo')),
        ]
    )
    start_time = models.TimeField(_('Hora de Início'))
    end_time = models.TimeField(_('Hora de Término'))

    class Meta:
        verbose_name = _('Disponibilidade do Médico')
        verbose_name_plural = _('Disponibilidades do Médico')
        unique_together = ('doctor', 'day_of_week', 'start_time', 'end_time')

    def __str__(self):
        return f'{self.doctor} - {self.get_day_of_week_display()} ({self.start_time} - {self.end_time})'
