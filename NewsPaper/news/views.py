# from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, UpdateView, CreateView, DeleteView
from .models import Post
from datetime import datetime
from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy

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
       context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
       context['form'] = PostForm()
       return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса
        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не накосячил, то сохраняем новый товар
            form.save()
        return super().get(request, *args, **kwargs)

class PostDetailView(DetailView):
   template_name = 'news/post_detail.html'
   queryset = Post.objects.all()

# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните. Остальное он сделает за вас
class PostCreateView(CreateView):
   template_name = 'news/post_create.html'
   form_class = PostForm

class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'

# дженерик для редактирования объекта
class PostUpdateView(UpdateView):
   template_name = 'news/post_create.html'
   form_class = PostForm

   def get_object(self, **kwargs):
       id = self.kwargs.get('pk')
       return Post.objects.get(pk=id)

class PostDeleteView(DeleteView):
   template_name = 'news/post_delete.html'
   queryset = Post.objects.all()
   success_url = reverse_lazy('news:posts')