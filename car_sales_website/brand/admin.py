from django.contrib import admin
from .import models
# Register your models here.

class BradnAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('Brand_Name',)}
    list_display = ['Brand_Name','slug']

admin.site.register(models.Brand, BradnAdmin)