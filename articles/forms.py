from django import forms
from .models import clients

class client_forms(forms.ModelForm):
    class Meta:
        model = clients
        fields = "__all__"
        
