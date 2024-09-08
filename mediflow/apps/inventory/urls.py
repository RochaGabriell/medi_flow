from django.urls import path
from .views import (
    InventoryListView,
    InventoryDetailView,
    InventoryCreateView,
    InventoryUpdateView,
    InventoryDeleteView
)

urlpatterns = [
    path('inventory/', InventoryListView.as_view(), name='inventory_list'),
    path(
        'inventory/<int:pk>/',
        InventoryDetailView.as_view(),
        name='inventory_detail'
    ),
    path('inventory/new/', InventoryCreateView.as_view(), name='inventory_create'),
    path(
        'inventory/<int:pk>/edit/',
        InventoryUpdateView.as_view(),
        name='inventory_update'
    ),
    path(
        'inventory/<int:pk>/delete/',
        InventoryDeleteView.as_view(),
        name='inventory_delete'
    ),
]
