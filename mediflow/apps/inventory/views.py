from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import InventoryModel

from mediflow.apps.appointments.models import AppointmentModel
from mediflow.apps.patients.models import PatientModel
from mediflow.apps.inventory.models import InventoryModel


class InventoryListView(ListView):
    model = InventoryModel
    template_name = 'inventory_list.html'
    context_object_name = 'inventory_items'


class InventoryDetailView(DetailView):
    model = InventoryModel
    template_name = 'inventory_detail.html'
    context_object_name = 'inventory_item'


class InventoryCreateView(CreateView):
    model = InventoryModel
    fields = ['name', 'quantity', 'minimum_quantity']
    template_name = 'inventory_form.html'
    success_url = reverse_lazy('inventory_list')


class InventoryUpdateView(UpdateView):
    model = InventoryModel
    fields = ['name', 'quantity', 'minimum_quantity']
    template_name = 'inventory_form.html'
    success_url = reverse_lazy('inventory_list')


class InventoryDeleteView(DeleteView):
    model = InventoryModel
    template_name = 'inventory_confirm_delete.html'
    success_url = reverse_lazy('inventory_list')


def report_dashboard(request):
    total_appointments = AppointmentModel.objects.count()
    total_patients = PatientModel.objects.count()
    total_inventory_items = InventoryModel.objects.count()

    context = {
        'total_appointments': total_appointments,
        'total_patients': total_patients,
        'total_inventory_items': total_inventory_items,
    }

    return render(request, 'report_dashboard.html', context)
