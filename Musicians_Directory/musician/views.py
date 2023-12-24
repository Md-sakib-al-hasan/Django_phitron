from django.shortcuts import render, redirect
from .import forms
from .import models
# Create your views here.
def add_musician (request):
    if request.method == 'POST':
        musician_from = forms.MusicianFrom(request.POST)
        if musician_from.is_valid():
            musician_from.save()
            return redirect('musician')
    else:
        musician_from= forms.MusicianFrom()
    return render(request, 'add_musician.html',{"form":musician_from})

def edit_musician (request,id):
    musician = models.Musicians.objects.get(pk=id)
    musician_from = forms.MusicianFrom(instance=musician)
    if request.method == 'POST':
        musician_from = forms.MusicianFrom(request.POST,instance=musician)
        if musician_from.is_valid():
            musician_from.save()
            return redirect('home')
        
    return render(request, 'add_musician.html',{"form":musician_from}) 