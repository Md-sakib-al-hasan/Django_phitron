<<<<<<< HEAD
from django.shortcuts import render
from car.models import Car
from brand.models import Brand
def home (request,brand_slug = None):
    data = Car.objects.all()
    if brand_slug is not None:
        ba = Brand.objects.get(slug = brand_slug)
        data = Car.objects.filter(Car_Brand_Name =ba)
    brand = Brand.objects.all()
    return render(request,'home.html',{'data':data,'brand':brand})
=======
from django.shortcuts import render
from car.models import Car
from brand.models import Brand
def home (request,brand_slug = None):
    data = Car.objects.all()
    if brand_slug is not None:
        ba = Brand.objects.get(slug = brand_slug)
        data = Car.objects.filter(Car_Brand_Name =ba)
    brand = Brand.objects.all()
    return render(request,'home.html',{'data':data,'brand':brand})
>>>>>>> 1536a79ed4bb132d457adca7cd486953d8e04534
