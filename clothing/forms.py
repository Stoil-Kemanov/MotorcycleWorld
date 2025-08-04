from django import forms

from clothing.models import Clothing


class ClothingCreationForm(forms.ModelForm):
    class Meta:
        model = Clothing
        fields = '__all__'
