from django.db import models
from car.models import Car
# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    Description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(Car,on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.name