<<<<<<< HEAD
from django import forms
from .import models 
class AlbumFrom(forms.ModelForm):
    class Meta:
        model = models.Album
=======
from django import forms
from .import models 
class AlbumFrom(forms.ModelForm):
    class Meta:
        model = models.Album
>>>>>>> 1536a79ed4bb132d457adca7cd486953d8e04534
        fields =  '__all__'