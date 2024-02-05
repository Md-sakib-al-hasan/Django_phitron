<<<<<<< HEAD
from django.shortcuts import render, redirect
from album.models import Album
# Create your views here.
def add_home (request):
    album_from = Album.objects.all()
=======
from django.shortcuts import render, redirect
from album.models import Album
# Create your views here.
def add_home (request):
    album_from = Album.objects.all()
>>>>>>> 1536a79ed4bb132d457adca7cd486953d8e04534
    return render(request, 'home.html',{"data":album_from})