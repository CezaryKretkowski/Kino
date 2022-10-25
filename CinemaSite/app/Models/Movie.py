from statistics import mode
from .Category import Category
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.name = models.ForeignKey(
        'Category', related_name='Movies', on_delete=models.CASCADE)
    time = models.IntegerField()
    description = models.TextField(max_length=1000)
    objects = models.Manager()
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.title
