from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/<int:id>/<str:nu>/',views.about, name= 'about')
]