from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Post


class BlogListView(ListView):
	"""Выводит список всех постов из БД"""
	model = Post 
	template_name = 'home.html' 


class BlogDetailView(DetailView):
	"""Осуществляет переход на выбранный пост"""
	model = Post
	template_name = 'post_detail.html'


class BlogCreateView(CreateView):
	"""Создает новый пост"""
	model = Post
	template_name = 'post_new.html'
	fields = "__all__"
	

class BlogUpdateView(UpdateView):
	"""Обновляет выбранный пост"""
	model = Post
	template_name = 'post_edit.html'
	fields = ['title', 'body']	


class BlogDeleteView(DeleteView):
	"""Удаляет пост из базы данных"""
	model = Post
	template_name = 'post_delete.html'
	success_url = reverse_lazy('home')