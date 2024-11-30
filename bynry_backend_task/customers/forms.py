from .models import ServiceRequest
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['customer_name', 'customer_email', 'request_description']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']