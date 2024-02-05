<<<<<<< HEAD
from django.db import models
from musician.models import Musicians
# Create your models here.
class Album (models.Model):
    Album_Name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musicians,on_delete = models.CASCADE)
    Album_release_date = models.DateField(auto_now_add=True)
    Rating_between = models.IntegerField()

    def __str__(self):
=======
from django.db import models
from musician.models import Musicians
# Create your models here.
class Album (models.Model):
    Album_Name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musicians,on_delete = models.CASCADE)
    Album_release_date = models.DateField(auto_now_add=True)
    Rating_between = models.IntegerField()

    def __str__(self):
>>>>>>> 1536a79ed4bb132d457adca7cd486953d8e04534
        return self.Album_Name