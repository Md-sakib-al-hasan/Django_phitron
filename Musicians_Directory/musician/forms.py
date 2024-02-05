from django import forms
from .import models

class MusicianFrom (forms.ModelForm):
    class Meta:
        model = models.Musicians
        fields = '__all__'