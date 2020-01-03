from django import forms
from . import models
class FormPost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = {
            'title',
            'author',
            'article',
        }
        labels = {
            'title':'Judul',
            'article':'Artikel',
            'author':'Penulis',
        }