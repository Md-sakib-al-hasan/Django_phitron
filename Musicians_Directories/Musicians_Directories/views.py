<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.views.generic import ListView
from album.models import Album
# Create your views here.
class home(ListView):
    model = Album
    template_name = 'home.html'
=======
from django.shortcuts import render, redirect
from django.views.generic import ListView
from album.models import Album
# Create your views here.
class home(ListView):
    model = Album
    template_name = 'home.html'
>>>>>>> 1536a79ed4bb132d457adca7cd486953d8e04534
    context_object_name = 'data'