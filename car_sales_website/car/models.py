from django.db import models
from brand.models import Brand
# Create your models here.
class Car(models.Model):
    Car_Name = models.CharField(max_length=100)
    Car_Price = models.DecimalField(max_digits=10, decimal_places=2)
    Car_Brand_Name = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="Brand")
    Description = models.TextField(null= True, blank=True)
    car_img = models.ImageField(null= True, blank=True)
    quantity =models.IntegerField(null= True, blank=True)

    def __str__(self):
        return self.Car_Name


