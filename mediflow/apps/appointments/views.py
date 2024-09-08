from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from datetime import timedelta
from datetime import datetime

from mediflow.apps.users.models import DoctorAvailabilityModel, DoctorModel
from .models import AppointmentModel
from .forms import AppointmentForm


class AppointmentCreateView(CreateView):
    model = AppointmentModel
    form_class = AppointmentForm
    template_name = 'appointment_form.html'
    success_url = reverse_lazy('appointment_availability')


class AppointmentAvailabilityView(ListView):
    model = DoctorAvailabilityModel
    template_name = 'appointment_availability.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.today().date()

        # Obtém todas as disponibilidades
        all_availabilities = DoctorAvailabilityModel.objects.all()

        # Cria um dicionário para armazenar as datas disponíveis por médico
        available_dates = {}

        for availability in all_availabilities:
            start_date = today
            # Defina o intervalo de um mês para exibição futura
            end_date = today + timedelta(days=30)
            current_date = start_date

            while current_date <= end_date:
                if current_date.weekday() == availability.day_of_week:
                    # Verifique se já existe um agendamento para este horário
                    if not AppointmentModel.objects.filter(
                        doctor=availability.doctor,
                        appointment_date=current_date
                    ).exists():
                        if availability.doctor not in available_dates:
                            available_dates[availability.doctor] = []
                        available_dates[availability.doctor].append(
                            current_date)

                current_date += timedelta(days=1)

        context['available_dates'] = available_dates
        return context


class DoctorAppointmentsView(ListView):
    model = AppointmentModel
    template_name = 'doctor_appointments.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        doctor_id = self.kwargs.get('doctor_id')
        return AppointmentModel.objects.filter(doctor_id=doctor_id).order_by('appointment_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctor_id = self.kwargs.get('doctor_id')
        context['doctor'] = DoctorModel.objects.get(id=doctor_id)
        return context


class AppointmentDeleteView(DeleteView):
    model = AppointmentModel
    template_name = 'appointment_confirm_delete.html'
    success_url = reverse_lazy('doctor_appointments')