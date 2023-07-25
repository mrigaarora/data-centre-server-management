from django import forms
from .models import *

class RacksForm(forms.ModelForm):
    class Meta:
        model = Rack
        fields = ['Rack']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company']

class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = '__all__'
