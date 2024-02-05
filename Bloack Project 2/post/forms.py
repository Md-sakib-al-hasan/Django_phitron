from django import forms
from .import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        # fields = '__all__'
        #fields = ['name','bio']
        exclude = ['author']