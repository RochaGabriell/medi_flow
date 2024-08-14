from django.contrib import admin
from .models import UserModel, DoctorModel

admin.site.register(UserModel)
admin.site.register(DoctorModel)
