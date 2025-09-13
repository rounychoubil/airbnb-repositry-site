
from django import forms
from .models import Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['date_in', 'date_out']
        widgets = {
            'date_out': forms.DateInput(attrs={'type': 'date'}),
            'date_in' : forms.DateInput(attrs={'type': 'date'})
        }