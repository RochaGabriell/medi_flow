from django.contrib import admin
from .models import UserModel, DoctorModel, DoctorAvailabilityModel

admin.site.register(UserModel)
admin.site.register(DoctorModel)
admin.site.register(DoctorAvailabilityModel)
