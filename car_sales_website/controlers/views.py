from typing import Any
from django.shortcuts import render , redirect
from .import forms
from car.models  import Car
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
    
class DetailPostView(DetailView):
    model = Car
    template_name = 'deatiles.html'
    pk_url_kwarg = 'id'

    def post(self, request, *args, **kwargs):
        car = self.get_object()
        comment_form = forms.CommentForm(data=self.request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    
@login_required()   
def profile(request):
    data_list = []
    print(car_list)
    for id in car_list:
        data = Car.objects.get(id = id)
        data_list.append(data)
    print("this is a profile")
    car_ids = [int(car_id) for car_id in car_list]
    print(car_ids)
    cars = Car.objects.filter(id__in=car_ids)
    for car in cars:
        print(car.Car_Name)
    return render(request,'profile.html',{'data': cars})
@login_required()
def change_user_data(request):
        if request.method == 'POST':
            form = forms.ChangeUserForm(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save()
        else:
            form = forms.ChangeUserForm(instance=request.user)
        return render(request, 'Change_user_data.html', {'form': form})
@login_required()
def Buy_now(request,id):
    car_instance = Car.objects.get(id=id)
    
    if car_instance.quantity is not None and car_instance.quantity != 0:
            car_list.append(id)
            car_instance.quantity -= 1
            messages.success(request,"This buy is successful")
    else:
        messages.success(request,"This car is stroke out")
    car_instance.save()
    
    print(car_list)
    return  redirect('profile')