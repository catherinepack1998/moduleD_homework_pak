# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime
from django.utils import timezone

class PostsList(ListView):
    model = Post
    template_name = 'news/posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-createData')

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['time_now'] = timezone.localtime(timezone.now())
       context['value1'] = None
       return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'