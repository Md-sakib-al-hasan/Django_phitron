from django.shortcuts import render, redirect
from album.models import Album
# Create your views here.
def add_home (request):
    album_from = Album.objects.all()
    return render(request, 'home.html',{"data":album_from})