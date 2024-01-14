from django.contrib.auth.models import User

from django import forms


from .models import *


class SeriesNameForm(forms.ModelForm):
    class Meta:
        model = SeriesName
        fields = ['createName', 'about', 'image']


class CharacterInfoForm(forms.ModelForm):
    class Meta:
        model = CharacterInfo
        fields = ['name', 'planet', 'quote', 'image', 'description']