from django.db import models
from book.models import Book
# Create your models here.
class Rating(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE, related_name="rating")
    RATING_CHOICES = [
        (1, 'One star'),
        (2, 'Two stars'),
        (3, 'Three stars'),
        (4, 'Four stars'),
        (5, 'Five stars'),
    ]
    rating = models.IntegerField(choices =RATING_CHOICES )

    def __str__(self):
        return self.rating