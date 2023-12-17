from django.db import models

# Create your models here.
class MyModel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    # big_auto_field = models.BigAutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()

    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()


    decimal_field = models.DecimalField(max_digits=5, decimal_places=2, default=9)
    email_field = models.EmailField(default="saka@gmail.com")


    duration_field = models.DurationField()


    file_field = models.FileField(upload_to='download (2).jpg')

    json_field = models.JSONField()

    uuid_field = models.UUIDField()

    url_field = models.URLField()

    time_field = models.TimeField()

    text_field = models.TextField()

    small_integer_field = models.SmallIntegerField()
    positive_small_integer_field = models.PositiveSmallIntegerField()
    positive_integer_field = models.PositiveIntegerField()
    
