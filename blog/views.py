from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'index.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name: str = 'post_new.html'
    fields = ['title', 'body', 'author']
