from django.shortcuts import render , redirect
from .import forms
from .import models
# from Post.forms import PostForm

# Create your views here.
def  add_post(request):
    if request.method == 'POST':
        Post_form = forms.PostForm(request.POST)
        if Post_form.is_valid():
            Post_form.save()
            return redirect('add_post')

    else:
       Post_form = forms.PostForm() 
    return render(request, 'add_Post.html',{'form':Post_form})

def  edit_post(request,id):
    post  = models.Post.objects.get(pk=id)
    Post_form = forms.PostForm(instance=post)

    if request.method == 'POST':
        Post_form = forms.PostForm(request.POST , instance=post)
        if Post_form.is_valid():
            Post_form.save()
            return redirect('home')


    return render(request, 'add_Post.html',{'form':Post_form})

def  delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('home')

   