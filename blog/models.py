from django.db import models


class Post(models.Model):

	title = models.CharField(max_length=200)
	author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	body = models.TextField()


	class Meta:
		verbose_name='Пост'
		verbose_name_plural = 'Посты'


	def __str__(self):
		return self.title