from django import forms

class djangoLoginForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    pic=forms.ImageField()
