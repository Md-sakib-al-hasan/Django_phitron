from django.shortcuts import render,redirect
from .import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,logout,login,update_session_auth_hash
# Create your views here.
def home (request):
    return render(request, 'home.html')

def signup (request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.SignupForm(request.POST)
            if form.is_valid():
                messages.success(request,'successfully signed up')
                form.save()
                return redirect('signup')
        else:
            form = forms.SignupForm()
        return render(request, 'signup.html',{'form':form})
    
    return render(request, 'profile.html',{'form':form})



def user_login (request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data= request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userPass = form.cleaned_data['password']
                user = authenticate(username = name, password = userPass)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    
    return render(request, 'profile.html',{'form':form})




def profile (request):
    if  request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.UserChangeForms(request.POST , instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            form = forms.UserChangeForms(instance=request.user)
        return render(request,'profile.html',{'form':form})
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})


def user_logout (request):
    if  request.user.is_authenticated:
        logout(request)
        return redirect('user_login')
    else:
        form = AuthenticationForm()
    return render(request,'profile.html',{'form':form})

def pass_change(request):
    if request.user.is_authenticated:
            if request.method == 'POST':
                form = PasswordChangeForm(user=request.user, data = request.POST)
                if form.is_valid():
                    form.save()
                    update_session_auth_hash(request, form.user)
                    return redirect('profile')
            else:
                form = PasswordChangeForm(user=request.user)
            return render(request,'change_pass_old.html',{'form':form})
    return redirect('home')

def change_pass_new(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request,'change_pass.html',{'form':form})
            
    return redirect('home')


            

