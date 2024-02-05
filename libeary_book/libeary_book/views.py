from django.shortcuts import render
from books.models import Book
from category.models import CategoryModel
def home (request,brand_slug = None):
    data = Book.objects.all()
    if brand_slug is not None:
        ba = CategoryModel.objects.get(slug = brand_slug)
        data = Book.objects.filter(book_category =ba)
    brand = CategoryModel.objects.all()
    return render(request,'home.html',{'data':data,'brand':brand})
