from typing import Any
from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from .import forms
from .import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView,DetailView

# from Post.forms import PostForm

# Create your views here.
@login_required
def  add_post(request):
    if request.method == 'POST':
        Post_form = forms.PostForm(request.POST)
        if Post_form.is_valid():
            # Post_form.cleaned_data['author'] = request.user
            Post_form.instance.author = request.user
            Post_form.save()
            return redirect('add_post')

    else:
       Post_form = forms.PostForm() 
    return render(request, 'add_Post.html',{'form':Post_form})



# add_post in class best view 
@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_Post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def  edit_post(request,id):
    post  = models.Post.objects.get(pk=id)
    Post_form = forms.PostForm(instance=post)

    if request.method == 'POST':
        Post_form = forms.PostForm(request.POST , instance=post)
        Post_form.instance.author = request.user
        if Post_form.is_valid():
            Post_form.save()
            return redirect('home')


    return render(request, 'add_Post.html',{'form':Post_form})

@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_Post.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)
 

@login_required
def  delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('home')

@method_decorator(login_required, name='dispatch')
class DeletePostview(DeleteView):
    model = models.Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'



class DetailsView(DetailView):
    model = models.Post
    template_name = 'post_details.html'
    pk_url_kwarg = 'id'
    
    def post(self, request, *args, **kwargs):
         if self.request.method == 'POST':
            post = self.get_object()
            comment_form = forms.CommentForm( data= self.request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.save()
            return self.get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context



   