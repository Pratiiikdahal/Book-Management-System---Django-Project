from .models import *
from django import forms

class add_author_form(forms.ModelForm):
    class Meta:
        model=Author
        fields='__all__'
        