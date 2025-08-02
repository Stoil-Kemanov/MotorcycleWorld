from django import forms

from motorcycles.choices import CategorySearch
from motorcycles.models import Motorcycle, MotorcycleParts, MotorcycleAccessories


class MotorcycleCreationForm(forms.ModelForm):
    class Meta:
        model = Motorcycle
        fields = '__all__'
        widgets = {
            'production_year': forms.NumberInput(attrs={'placeholder': 'Year (1800-2025)'}),
            'engine_power': forms.NumberInput(attrs={'placeholder': 'Engine power in HP'}),
            'engine_volume': forms.NumberInput(attrs={'placeholder': 'Engine volume in CC'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price in EUR'}),
        }


class MotorcyclePartsCreationForm(forms.ModelForm):
    class Meta:
        model = MotorcycleParts
        fields = '__all__'


class MotorcycleAccessoriesCreationForm(forms.ModelForm):
    class Meta:
        model = MotorcycleAccessories
        fields = '__all__'


class UniversalSearchForm(forms.Form):

    search = forms.CharField(max_length=100, required=False,
                             widget=forms.TextInput(attrs={'placeholder': 'Search motorcycles, parts, accessories...'}))
    category = forms.ChoiceField(choices=CategorySearch, required=False)
    min_price = forms.DecimalField(max_digits=10, decimal_places=2, required=False,
                                   widget=forms.NumberInput(attrs={'placeholder': 'Minimum price in EUR'}))
    max_price = forms.DecimalField(max_digits=10, decimal_places=2, required=False,
                                   widget=forms.NumberInput(attrs={'placeholder': 'Maximum price in EUR'}))
