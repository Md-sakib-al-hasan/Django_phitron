from django.shortcuts import render , redirect
from .import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from post.models import Post
# from author.forms import AuthorForm

# Create your views here.
# def  add_author(request):
#     if request.method == 'POST':
#         author_form = forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#         return redirect('add_author')

#     else:
#        author_form = forms.AuthorForm() 
#     return render(request, 'add_author.html',{'form':author_form}) 


def register(request):
    if  request.method == 'POST':
        register_from = forms.RegistrationForm(request.POST)
        if register_from.is_valid():
            messages.success(request,"Account created successfully")
            register_from.save()
            return redirect('register')
    else:
        register_from = forms.RegistrationForm()
    return render(request, 'register.html',{'form':register_from,'type':'register'}) 


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data= request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userPass = form.cleaned_data['password']
            user = authenticate(username = name, password = userPass)
            if user is not None:
                messages.success(request,"Logged in successfully")
                login(request, user)
                return redirect('profile')
            else:
                messages.success(request,"Login informtion in incorrect")
                return redirect('register')
        else:
            messages.success(request,"Login informtion in incorrect")
            return redirect('register')

    else:
        form = AuthenticationForm()
        return render(request, 'register.html',{'form':form,'type':'Login'})
    
@login_required
def Profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html',{'data':data})

@login_required
def edit_profile(request):
    if  request.method == 'POST':
        profile_from = forms.ChangeUserForm(request.POST ,instance = request.user)
        if profile_from.is_valid():
            messages.success(request,"Profile update successfllly")
            profile_from.save()
            return redirect('profile')
    else:
        profile_from = forms.ChangeUserForm(instance = request.user)
    return render(request, 'update_profile.html',{'form':profile_from})


def Passchnagen(request):
    if  request.method == 'POST':
        pass_change = PasswordChangeForm(user= request.user , data = request.POST)
        if pass_change.is_valid():
            messages.success(request,"password change successfully")
            pass_change.save()
            update_session_auth_hash(request, pass_change.user)
            return redirect('profile')
    else:
        pass_change =PasswordChangeForm(user= request.user)
    return render(request, 'pass_change.html',{'form':pass_change})

def User_logout(request):
    logout(request)
    return redirect('user_login')

