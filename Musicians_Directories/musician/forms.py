<<<<<<< HEAD
from django import forms
from .import models

class MusicianFrom (forms.ModelForm):
    class Meta:
        model = models.Musicians
=======
from django import forms
from .import models

class MusicianFrom (forms.ModelForm):
    class Meta:
        model = models.Musicians
>>>>>>> 1536a79ed4bb132d457adca7cd486953d8e04534
        fields = '__all__'