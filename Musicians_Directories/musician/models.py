<<<<<<< HEAD
from django.db import models

# Create your models here.
class Musicians(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email =  models.EmailField()
    Phone_number = models.CharField(max_length=12)
    Instrument_Type = models.CharField(max_length=100)

    def __str__(self):
=======
from django.db import models

# Create your models here.
class Musicians(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email =  models.EmailField()
    Phone_number = models.CharField(max_length=12)
    Instrument_Type = models.CharField(max_length=100)

    def __str__(self):
>>>>>>> 1536a79ed4bb132d457adca7cd486953d8e04534
        return self.First_name