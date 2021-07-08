from django.views.generic import ListView, DeleteView
from  .models import *


class HomeView(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'


class PostDetailView(DeleteView):
    model = Post
    template_name = 'post/post-detail.html'
    context_object_name = 'post'


class PostByCategory(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts' 

    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        posts = Post.objects.filter(category__slug=category_slug)
        return posts 