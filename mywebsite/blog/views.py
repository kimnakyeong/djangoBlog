from django.shortcuts import render
from blog.models import Category, Post
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
def index(req):
    post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        "post_latest": post_latest
    }

    return render(req, "index.html", context = context)

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post_list'

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "title_image", "context", "category"]

class PostDelete(DeleteView):
    model = Post
    success_url = '/'
    context_object_name = 'post_list'

class PostUpdate(UpdateView):
    model = Post
    fields = ["title", "title_image", "context", "category"]
    context_object_name = 'post_list'

    
    


# def single(req):
#     context = {

#     }
    
#     return render(req, "single.html", context = context)