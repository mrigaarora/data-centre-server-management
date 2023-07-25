from django import forms
from .models import *
from smart_selects.form_fields import ChainedModelChoiceField
from smart_selects.widgets import ChainedSelect


class RacksForm(forms.ModelForm):
    class Meta:
        model = Rack
        fields = '__all__'


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


    
class ServerForm(forms.ModelForm):    
    class Meta:
        model = Server
        fields = '__all__'
        widgets = {
            'vm_information_file': forms.ClearableFileInput(attrs={'multiple': True})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ownership'].queryset = OwnershipChoice.objects.order_by('display_name')

    

    