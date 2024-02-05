<<<<<<< HEAD
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView
from .import models
from .import forms
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(login_required, name= "dispatch")
class musician(CreateView):
    model =models.Musicians
    form_class = forms.MusicianFrom
    template_name = 'add_musicians.html'
    success_url = reverse_lazy('home')
@method_decorator(login_required, name= "dispatch")
class Edit_musician(UpdateView):
    model =models.Musicians
    pk_url_kwarg = 'id'
    form_class = forms.MusicianFrom
    template_name = 'add_musicians.html'
=======
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView
from .import models
from .import forms
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(login_required, name= "dispatch")
class musician(CreateView):
    model =models.Musicians
    form_class = forms.MusicianFrom
    template_name = 'add_musicians.html'
    success_url = reverse_lazy('home')
@method_decorator(login_required, name= "dispatch")
class Edit_musician(UpdateView):
    model =models.Musicians
    pk_url_kwarg = 'id'
    form_class = forms.MusicianFrom
    template_name = 'add_musicians.html'
>>>>>>> 1536a79ed4bb132d457adca7cd486953d8e04534
    success_url = reverse_lazy('home')