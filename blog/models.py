from django.db import models
from django.urls import reverse


class Post(models.Model):
	"""Модельб отражающая структуру поста в БД"""
	title = models.CharField(max_length=200)
	author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	body = models.TextField()


	class Meta:
		verbose_name='Пост'
		verbose_name_plural = 'Посты'


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', args=[str(self.id)] )

