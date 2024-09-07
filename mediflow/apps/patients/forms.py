from django import forms

from .models import PatientModel


class PatientForm(forms.ModelForm):

    class Meta:
        model = PatientModel
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
