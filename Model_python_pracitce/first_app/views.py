from django.shortcuts import render
from first_app.forms import MyModelForm

# Create your views here.
def home(request):
    sk = MyModelForm()
    return render(request, 'home.html',{'sk':sk})
