from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    body = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    photo = models.FileField(upload_to='media/%Y/%m/%d/', blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True
                                ,verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')


    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

