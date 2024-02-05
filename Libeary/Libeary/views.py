from django.shortcuts import render
from book.models import Book
from brand.models import Brand
# def home (request,brand_slug = None):
#     data = Book.objects.all()
#     if brand_slug is not None:
#         ba = Brand.objects.get(slug = brand_slug)
#         data = Book.objects.filter(Car_Brand_Name =ba)
#     brand = Brand.objects.all()
#     return render(request,'home.html',{'data':data,'brand':brand})

def home (request):
    return render(request,'home.html')
