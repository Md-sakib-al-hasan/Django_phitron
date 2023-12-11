
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('first_app/',include("First_app.urls"))
]
