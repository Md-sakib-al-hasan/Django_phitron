from django.contrib import admin
from .import models
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_title',)}
    list_display = ['category_title','slug']

admin.site.register(models.CategoryModel, CategoryAdmin)