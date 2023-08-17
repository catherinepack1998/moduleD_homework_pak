# from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Post
from datetime import datetime
from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator
from .filters import ProductFilter

class PostsList(ListView):
    model = Post
    template_name = 'news/posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-createData')
    paginate_by = 10

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['time_now'] = timezone.localtime(timezone.now())
       context['value1'] = None
       context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
       return context

class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'