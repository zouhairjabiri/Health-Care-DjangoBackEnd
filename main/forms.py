from django import forms
from .models import Patient

class PatientForm(forms.ModelForm): 
    
    class Media:
        js = ('main/js/base.js',)