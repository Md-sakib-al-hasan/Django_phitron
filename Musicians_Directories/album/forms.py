from django import forms
from .import models 
class AlbumFrom(forms.ModelForm):
    class Meta:
        model = models.Album
        fields =  '__all__'