from django.contrib.auth.forms import UserCreationForm
from django import forms
from datetime import datetime

from django.core.exceptions import ValidationError

from accounts.models import MotoUser, Profile, OwnedMotorcycle


class MotoUserCreationForm(UserCreationForm):
    class Meta:
        model = MotoUser
        fields = ['email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    date_of_birth = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'DD/MM/YYYY'})
    )

    def clean_date_of_birth(self):
        date_str = self.cleaned_data.get('date_of_birth')
        if not date_str:
            return None
        try:
            return datetime.strptime(date_str, '%d/%m/%Y').date()
        except ValueError:
            raise ValidationError('Please use DD/MM/YYYY format')

    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'height' : forms.NumberInput(attrs={'placeholder': 'cm'}),
            'weight' : forms.NumberInput(attrs={'placeholder': 'kg'}),
        }


class OwnedMotorcycleForm(forms.ModelForm):
    class Meta:
        model = OwnedMotorcycle
        exclude = ['user']

