from django.contrib import admin
from .models import BillingModel, PaymentModel

admin.site.register(BillingModel)
admin.site.register(PaymentModel)