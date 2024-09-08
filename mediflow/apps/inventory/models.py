from django.db import models
from django.utils.translation import gettext_lazy as _


class InventoryModel(models.Model):

    name = models.CharField(_('Nome'), max_length=255)
    quantity = models.PositiveIntegerField(_('Quantidade'), default=0)
    minimum_quantity = models.PositiveIntegerField(
        _('Quantidade Mínima'),
        default=0
    )
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    def is_below_minimum(self):
        return self.quantity < self.minimum_quantity
