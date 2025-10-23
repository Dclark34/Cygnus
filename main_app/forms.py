from django import forms
from .models import Sighting, Bird

class SightingForm(forms.ModelForm):
    class Meta:
        model = Sighting
        fields = ['location', 'date', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }