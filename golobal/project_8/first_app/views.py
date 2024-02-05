from django.shortcuts import render, redirect
from .import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def sign(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,'successfully registered')
            form.save()
            print(form.cleaned_data)
    else:
        form = forms.RegisterForm(request.POST)
    return render(request, 'sigine.html',{'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass=form.cleaned_data['password']
                user = authenticate(username=name, password=userpass)
                if user is not  None:
                    login(request, user)
                    return redirect ('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html',{'form':form})
    else:
        return redirect('home')

def profile (request):
    sk = request.user
    return render(request,'profile.html',{'user':sk})

def home(request):
    return render(request, 'home.html')
