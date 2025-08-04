from django import forms

from services.models import Service


class ServiceCreationForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
