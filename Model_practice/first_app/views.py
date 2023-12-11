from django.shortcuts import render
from first_app.forms import LoginForm
from .import models

# Create your views here.

def home(request):

    if request.method == 'POST':
        sk = LoginForm(request.POST)
        if sk.is_valid():
            sk.save()
    else:
       sk = LoginForm(request.POST)
    
    return render(request,'home.html',{'form':sk})


def delet_data(request,id):
    std = models.LoginModel.objects.get(pk=id)
    print(std)
    
    return render(request,'home.html',)


