from django.urls import path
from .import views
urlpatterns = [
    path('',views.loginHome, name='home'),
    path('form/',views.loginForm, name='form'),
    path('django_form/',views.django_loginForm, name='django_form'),
]
