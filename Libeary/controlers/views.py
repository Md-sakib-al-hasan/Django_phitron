from typing import Any
from django.shortcuts import render , redirect
from .import forms
from . import  models
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.views.generic import DetailView

# Create your views here.
# array
car_list = []
car_list = list(dict.fromkeys(car_list))

def Register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            register_form = forms.RegistrationForm(request.POST)
            if register_form.is_valid():
                messages.success(request,'Login successful')
                register_form.save()
                return redirect('login')
        else:
            register_form = forms.RegistrationForm(request.POST)
        return render(request, 'signup.html',{'form':register_form})
    else:
        return redirect('home')
    
class userLoginView(LoginView):
        template_name = 'signup.html'
        def get_success_url(self): 
            return reverse_lazy('profile')
    
class userLogoutView( LogoutView):
    template_name = 'home'
    def get_success_url(self): 
        car_list.clear()
        return reverse_lazy('login')
    
