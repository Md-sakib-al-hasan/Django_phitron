from django.shortcuts import render,redirect
from .forms import RegisterForm , changeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form  = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request,"Account has been registered")
                # messages.warning(request,"warning account")
                # messages.info(request,"info")
                form.save()
                print(form.cleaned_data)
        else: 
            form  = RegisterForm()
        return render(request, 'signup.html',{'form':form})
    else:
        return redirect('profile')

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            users = authenticate(username = name, password = userpass)
            if users is not None:
                login(request, users)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})
    
def profile(request):
    if  request.user.is_authenticated:
        if request.method == "POST":
            form  = changeUserData(request.POST , instance = request.user)
            if form.is_valid():
                messages.success(request,"Account has been udatesuccesully")
                # messages.warning(request,"warning account")
                # messages.info(request,"info")
                form.save()
                print(form.cleaned_data)
        else: 
            form  = changeUserData(instance = request.user)
        return render(request, 'profile.html',{'form':form})
    else:
        return redirect('signup')
 
   

def  user_logout(request):
      logout(request)
      return redirect('login')

def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user , data= request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'passchange.html',{'form':form})


def pass_change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user , data= request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request,'passchange.html',{'form':form})


