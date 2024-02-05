<<<<<<< HEAD
from django.shortcuts import render
from FormsAPI.forms import LoginForm

# Create your views here.
def Forms(request):
    From = LoginForm

=======
from django.shortcuts import render
from FormsAPI.forms import LoginForm

# Create your views here.
def Forms(request):
    From = LoginForm

>>>>>>> 1536a79ed4bb132d457adca7cd486953d8e04534
    return render(request,'FormsAPI/Forms.html',{'from':From} )