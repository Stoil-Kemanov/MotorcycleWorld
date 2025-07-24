from django.contrib.auth.forms import UserCreationForm
from django import forms

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
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'date_of_birth' : forms.DateInput(attrs={'type': 'date'}),
            'height' : forms.NumberInput(attrs={'placeholder': 'cm'}),
            'weight' : forms.NumberInput(attrs={'placeholder': 'kg'}),
        }


class OwnedMotorcycleForm(forms.ModelForm):
    class Meta:
        model = OwnedMotorcycle
        exclude = ['user']

