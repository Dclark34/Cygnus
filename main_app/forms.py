from django import forms
from .models import Sighting, Bird, SightingBird

class SightingForm(forms.ModelForm):
    class Meta:
        model = Sighting
        fields = ['location', 'date', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

#Form to add a bird to a sighting. Will show a drop-down menu of all birds, while allowing us to select how many of said bird we see in that sighting.
class AddBirdToSightingForm(forms.ModelForm):
    bird = forms.ModelChoiceField(
        queryset=Bird.objects.all(), #makes all birds in db available as choices.
        widget=forms.Select(attrs={'class' : 'form-control'}) # form-control is like the widget. we're doing a dropdown menu for this atm. Will be refactored to search here I think.
    )
    class Meta:
        model=SightingBird
        fields= ['bird', 'quantity']
        widgets = {
            'quantity' : forms.NumberInput(attrs={'class': 'form-control', 'min': 1}), #number input with default to one
        }

#!ice box. change this feature to a search bar / autocomplete dropdown menu.