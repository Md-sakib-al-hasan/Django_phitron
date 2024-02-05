from django.db import models
from category.models import CategoryModel
# Create your models here.
class Book(models.Model):
    book_Name = models.CharField(max_length=100)
    book_Price = models.DecimalField(max_digits=10, decimal_places=2)
    book_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="category")
    Description = models.TextField(null= True, blank=True)
    book_img = models.ImageField(null= True, blank=True)

    def __str__(self):
        return self.book_Name


