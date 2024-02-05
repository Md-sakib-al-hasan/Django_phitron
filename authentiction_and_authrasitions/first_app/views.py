from django.shortcuts import render,redirect
from .import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.
def home (request):
    return render(request, 'home.html',{'type':'Home'})

def signup (request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,"Successfully  signed up")
            form.save()
            return redirect('User_login')
    else:
        form = forms.RegisterForm(request.POST)
    return render(request, 'signup.html',{'form':form})

def User_login (request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request , data = request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userPass = form.cleaned_data['password']
            user = authenticate(username= name, password= userPass)
            if user is not None:
                login(request, user)
                messages.success(request,"Successfully login")
                return redirect('Profile')
            else:
                form = AuthenticationForm(request=request , data = request.POST)
            return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request, 'signup.html',{'form':form})

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def user_logout(request):
    messages.success(request,"Successfully logout")
    logout(request)
    return redirect('home')

@login_required
def old_password (request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user , data = request.POST)
        if form.is_valid():
            messages.success(request,"Successfully change password")
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('Profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'signup.html',{'form':form})

@login_required
def old_password2 (request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user , data = request.POST)
        if form.is_valid():
            messages.success(request,"Successfully change password")
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('Profile')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'signup.html',{'form':form})