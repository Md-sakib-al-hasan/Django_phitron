from django.db import models
from books.models import Book
from django.contrib.auth.models import User
# Create your models here.
class Rating(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE, related_name="ratings")
    user = models.OneToOneField(User, related_name='rating_user', on_delete=models.CASCADE, blank=True,null=True)
    RATING_CHOICES = [
        (1, 'One star'),
        (2, 'Two stars'),
        (3, 'Three stars'),
        (4, 'Four stars'),
        (5, 'Five stars'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.book.book_Name
    
class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    deposit_type = models.CharField(max_length=50, blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)