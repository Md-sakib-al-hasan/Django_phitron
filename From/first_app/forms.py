from django import forms 
from django.core import validators

class LoginForm(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10,"sakib")])
    email = forms.EmailField()

    # def clean_name(self):
    #      valname = self.cleaned_data.get('name')

    #      if len(valname) <5:
    #           raise forms.ValidationError("please enter")

    # def clean_email(self):
    #      valemail = self.cleaned_data.get('email')

    #      if 's' not in valemail:
    #           raise forms.ValidationError("s mising")
         
    # def clean(self):
    #      cleaned_data = super().clean()
    #      valname = self.cleaned_data.get('name')
    #      valemail = self.cleaned_data.get('email')

    #      if len(valname) <5:
    #           raise forms.ValidationError("please enter")
         
    #      if 's' not in valemail:
    #           raise forms.ValidationError("s mising")
         
         

         



    # ch =[('s','small',),('l','medium')]
    # check = forms.ChoiceField(choices=ch)
    # chm=[('s','spice'),('p','pizza'),('sp','sope')]
    # multicheck = forms.MultipleChoiceField(choices=chm, widget=forms.CheckboxSelectMultiple)
