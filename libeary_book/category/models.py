from django.db import models

# Create your models here.

class CategoryModel (models.Model):
    category_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.category_title 
