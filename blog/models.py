from django.db import models
from django.utils.text import slugify
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    article = models.TextField()
    author = models.CharField(max_length=50)
    slug = models.SlugField()
    def save(self):
        self.slug = slugify(self.title)
        super(Post,self).save()
    def __str__(self):
        return '{}.{}'.format(self.id,self.title)
