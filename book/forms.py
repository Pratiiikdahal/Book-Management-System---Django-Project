from django import forms  
from .models import *

class addbook_form(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'
