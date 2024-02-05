from django.db import models

# Create your models here.

class Brand (models.Model):
    Brand_Name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.Brand_Name
