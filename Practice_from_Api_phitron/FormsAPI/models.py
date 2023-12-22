from django.db import models
import datetime

# Create your models here.
# class movies(models.Model):
#     name= models.CharField(max_length=20)
#     age= models.IntegerField()

#     def __str__(self):
#         return self.name
class MyModule1(models.Model):
    auto_field = models.AutoField(primary_key=True)
    name = models.CharField(default="uk")
    # def __str__(self):
    #     return "AutoField"

# class MyModule2(models.Model):
#     name = models.CharField(max_length=20 ,default="sakib")
    # models.BigAutoField(primary_key=True)
    # boolean_field = models.BooleanField()
    # char_field = models.CharField(max_length=255)
    # date_field = models.DateField()
    # date_time_field = models.DateTimeField()

    # decimal_field = models.DecimalField(max_digits=5, decimal_places=5,default=5)
    # duration_field = models.DurationField()
    # email_field = models.EmailField()
    # file_field = models.FileField(upload_to='./static')
    # file_path_field = models.FilePathField(path='./templates/FormsAPI',default='FormsAPI/forms.html')
    # float_field = models.FloatField(default=3.5)
    # generic_ip_address_field = models.GenericIPAddressField(default=14)

    # image_field = models.ImageField(upload_to='./static/download (2).jpg')
    # integer_field = models.IntegerField(default=12)
#     json_field = models.JSONField(default={
#   "MyModel": {
#     "comma_separated_field": {
#       "type": "CharField",
#       "validators": [
#         {
#           "name": "comma_separated_validator"
#         }
#       ],
#       "max_length": 255
#     }
#   }
# }
# )
    # many_to_many_field = models.ManyToManyField(MyModule1)

    # null_boolean_field = models.NullBooleanField()
    # one_to_one_field = models.OneToOneField(MyModule1, on_delete=models.CASCADE)
    # slug_field = models.SlugField()

    # small_integer_field = models.SmallIntegerField(default=14)
    # text_field = models.TextField(default="kmal")
    # time_field = models.TimeField(default=datetime.datetime.today())
    # url_field = models.URLField(default="http://google.ocm")
    # uuid_field = models.UUIDField(default="aaakddkdk34")
    # positive_big_integer_field = models.PositiveBigIntegerField(default=14)
    # positive_small_integer_field = models.PositiveSmallIntegerField(default=30)
    
    