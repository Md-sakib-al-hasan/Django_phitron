from django.shortcuts import render, redirect
from .import forms
from .import models
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(login_required, name= "dispatch")
class album(CreateView):
    model =models.Album
    form_class = forms.AlbumFrom
    template_name = 'add_album.html'
    success_url = reverse_lazy('home')
@method_decorator(login_required, name= "dispatch")
class delete_album(DeleteView):
    model =models.Album
    template_name = 'delete_album.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
@method_decorator(login_required, name= "dispatch")
class Edit_album(UpdateView):
    model =models.Album
    form_class = forms.AlbumFrom
    template_name = 'add_album.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'


