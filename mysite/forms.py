# forms.py
from django import forms
from .models import Card
from django import forms
from django.contrib.auth.models import User

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['name', 'image']
