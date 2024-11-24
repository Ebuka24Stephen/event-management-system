from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.title