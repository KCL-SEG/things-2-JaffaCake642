"""Forms of the project."""
from enum import unique
from django import forms
from .models import Thing

# Create your forms here.

class ThingForm(forms.ModelForm):
    # name = forms.CharField(max_length=35, required=False)
    # description = forms.Textarea(max_length=120, required=False)
    # quantity = forms.NumberInput(attrs={'min':0, 'max': 50})
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = { 'description':forms.Textarea(), 'quantity':forms.NumberInput() }