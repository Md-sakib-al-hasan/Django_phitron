from django.db import models

# Create your models here.
class LoginModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=120)
    birthday = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
