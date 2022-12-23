from django import forms
from .models import Category, Post


# class PostForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Название:')
#     body = forms.CharField(label='Содержимое:')
#     category = forms.ModelChoiceField(empty_label='Выберите категорию', queryset=Category.objects.all(), label='Категория')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'body', 'category']
        #widgets = {}
