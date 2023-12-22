from django.shortcuts import render , redirect
from post.models import Post
# from Post.forms import PostForm

# Create your views here.
def home(request):
    data = Post.objects.all()
    return render(request, 'home.html',{"data": data})