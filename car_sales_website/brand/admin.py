<<<<<<< HEAD
from django.contrib import admin
from .import models
# Register your models here.

class BradnAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('Brand_Name',)}
    list_display = ['Brand_Name','slug']

=======
from django.contrib import admin
from .import models
# Register your models here.

class BradnAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('Brand_Name',)}
    list_display = ['Brand_Name','slug']

>>>>>>> 1536a79ed4bb132d457adca7cd486953d8e04534
admin.site.register(models.Brand, BradnAdmin)