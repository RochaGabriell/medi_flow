from django.urls import path

from .views import (
    AppointmentCreateView,
    AppointmentAvailabilityView,
    DoctorAppointmentsView,
    AppointmentDeleteView
)

urlpatterns = [
    path(
        'agendamento/',
        AppointmentCreateView.as_view(),
        name='appointment_create'
    ),
    path(
        'disponibilidade/',
        AppointmentAvailabilityView.as_view(),
        name='appointment_availability'
    ),
    path(
        'consultas/<int:doctor_id>/',
        DoctorAppointmentsView.as_view(),
        name='doctor_appointments'
    ),
    path(
        'consulta/delete/<int:pk>/',
        AppointmentDeleteView.as_view(),
        name='delete_appointment'
    ),
]
