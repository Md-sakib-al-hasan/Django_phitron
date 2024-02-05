from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .import models
from django import forms
from .models import Deposit

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget = forms.TextInput(attrs = {'id':'required'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs = {'id':'required'}))
    class Meta:
        model = User
        fields =['username', 'first_name', 'last_name', 'email']

class ChangeUserForm(UserChangeForm):
    password= None
    class Meta:
        model = User
        fields =['username', 'first_name', 'last_name', 'email']

class RatingForm(forms.ModelForm):
    class Meta:
        model = models.Rating
        fields = ['rating']

class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['amount', 'deposit_type', 'purpose']
