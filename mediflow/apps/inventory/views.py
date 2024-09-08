from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import InventoryModel


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
