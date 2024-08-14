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
        _('Role'),
        max_length=20,
        choices=ROLE_CHOICES,
        default='patient'
    )


class DoctorModel(models.Model):

    user = models.OneToOneField(
        UserModel,
        on_delete=models.PROTECT,
    )
    crm = models.CharField(_('CRM'), max_length=20)
    especiality = models.CharField(_('Especiality'), max_length=255)
