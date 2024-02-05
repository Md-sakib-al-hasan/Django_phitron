from django.shortcuts import render
from .import forms
# Create your views here.
def loginHome(request):
     if request.method == 'POST':
        print(request.POST.get('name'))
        name = request.POST.get('name')
        email = request.POST.get('email')
        pic = request.POST.get('pic')
        print(request.POST.get('pic'))
        
        if pic is not None:

            return render(request,'login_home.html',{'name':name, 'email':email,'pic':pic})
        else:
            return render(request,'login_home.html',{'name':name, 'email':email})
     else:
        return render(request,'login_home.html')

def loginForm(request):
    return render(request,'login_form.html')

def django_loginForm(request):
    sdj_form = forms.djangoLoginForm()
    return render(request,'django_loginForm.html',{'form':sdj_form})
