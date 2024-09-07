from django import forms
from .models import UserModel


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'first_name', 'last_name']


class UserSearchForm(forms.Form):
    query = forms.CharField(required=False, label='Search')
