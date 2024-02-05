from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('user_login/',views.user_login,name='user_login'),
    path('profile/',views.profile,name='profile'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('pass_change/',views.pass_change,name='pass_change'),
    path('pass_change_new/',views.change_pass_new,name='pass'),
   
]