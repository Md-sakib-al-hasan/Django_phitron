from django.shortcuts import render , redirect
from .import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy

# Create your views here.

class SignupForm(CreateView):
     form_class = forms.RegistrationForm
     template_name = 'user.html'
     success_url = reverse_lazy('signup')

class user_login(LoginView):
     template_name = 'user.html'
     def get_success_url(self):
          return reverse_lazy('home')
class user_logout(LogoutView):
     def get_success_url(self):
          return reverse_lazy('home')