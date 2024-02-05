from django.urls import path
from .import views
urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('sign/',views.sign,name='sign'),
    path('profile/',views.profile,name='profile'),
    path('',views.home,name='home'),
]
