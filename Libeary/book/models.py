from django.db import models
from brand.models import Brand
# Create your models here.
class Book(models.Model):
    Book_Name = models.CharField(max_length=100)
    Book_Price = models.DecimalField(max_digits=10, decimal_places=2)
    Book_Brand_Name = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="brand")
    Description = models.TextField(null= True, blank=True)
    Book_img = models.ImageField(null= True, blank=True)

    def __str__(self):
        return self.Book_Name


