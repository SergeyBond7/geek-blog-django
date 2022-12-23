from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import PostForm


class HomePost(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


# Home Page
# def index(request):
#     post = Post.objects.all()
#     return render(request, 'home.html', {'post': post})
#
#


class PostsByCategory(ListView):
    model = Category
    template_name = 'post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(category_id=self.kwargs['category_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post_item'


class AddPost(CreateView):
    form_class = PostForm
    template_name = 'add_post.html'


# Filter by category
# def get_category(request, category_id):
#     post = Post.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'category.html', {'post': post,
#                                              'category': category})


# def post_detail(request, post_id):
#     post_item = get_object_or_404(Post, pk=post_id)
#     return render(request, 'post_detail.html', {"post_item": post_item})



# Post adding
# def add_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             # post = Post.objects.create(**form.cleaned_data)
#             post = form.save()
#             return redirect(post)
#     else:
#         form = PostForm()
#     return render(request, 'add_post.html', {'form': form})