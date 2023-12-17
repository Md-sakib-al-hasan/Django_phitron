from django.shortcuts import render
from FormsAPI.forms import LoginForm

# Create your views here.
def Forms(request):
    From = LoginForm

    return render(request,'FormsAPI/Forms.html',{'from':From} )