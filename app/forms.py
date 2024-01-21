from django import forms
from app.models import *




class Topic(forms.Form):
    class Meta():
        model=Topic
        fields='__all__'