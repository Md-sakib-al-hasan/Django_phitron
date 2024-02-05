from django.shortcuts import render, redirect
from .import forms
from .import models
# Create your views here.
def add_album (request):
    if request.method == 'POST':
        album_from = forms.AlbumFrom(request.POST)
        if album_from.is_valid():
            album_from.save()
            return redirect('album')
    else:
        album_from= forms.AlbumFrom()
    return render(request, 'add_album.html',{"form":album_from})

def edit_album (request,id):
    album = models.Album.objects.get(pk=id)
    album_from = forms.AlbumFrom(instance=album)
    if request.method == 'POST':
        album_from = forms.AlbumFrom(request.POST,instance=album)
        if album_from.is_valid():
            album_from.save()
            return redirect('home')
        
    return render(request, 'add_album.html',{"form":album_from})

def delete_album (request,id):
    album = models.Album.objects.get(pk=id)
    album.delete()
    return redirect('home')