from django.shortcuts import render , redirect
from post.models import Post
from categories.models import Category
# from Post.forms import PostForm

# Create your views here.
def home(request , category_slug=None):
    data = Post.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug=category_slug)
        data  = Post.objects.filter(category = category)
    Categories = Category.objects.all()
    return render(request, 'home.html',{"data": data,'category':Categories})
