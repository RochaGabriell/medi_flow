from django.core.exceptions import ValidationError
from django import forms

from mediflow.apps.users.models import DoctorAvailabilityModel
from .models import AppointmentModel


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = AppointmentModel
        fields = '__all__'
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        appointment_date = cleaned_data.get('appointment_date')
        doctor = cleaned_data.get('doctor')

        if appointment_date and doctor:
            # Verifica se já existe um agendamento para o médico e a data selecionada
            if AppointmentModel.objects.filter(doctor=doctor, appointment_date=appointment_date).exists():
                raise ValidationError(
                    "Este horário já está ocupado para este médico.")

            # Opcional: Verifique se a data está dentro dos horários disponíveis do médico
            availability = DoctorAvailabilityModel.objects.filter(
                doctor=doctor,
                day_of_week=appointment_date.weekday()
            )

            if not availability.exists():
                raise ValidationError(
                    "Não há disponibilidade para este médico na data selecionada.")

        return cleaned_data
