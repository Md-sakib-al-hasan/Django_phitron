from django.shortcuts import render, redirect
from django.views.generic import ListView
from album.models import Album
# Create your views here.
class home(ListView):
    model = Album
    template_name = 'home.html'
    context_object_name = 'data'