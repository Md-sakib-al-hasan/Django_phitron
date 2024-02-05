<<<<<<< HEAD
from django.db import models

# Create your models here.

class Brand (models.Model):
    Brand_Name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.Brand_Name
=======
from django.db import models

# Create your models here.

class Brand (models.Model):
    Brand_Name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.Brand_Name
>>>>>>> 1536a79ed4bb132d457adca7cd486953d8e04534
