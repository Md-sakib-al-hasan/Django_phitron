from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('User_login/',views.User_login,name='User_login'),
    path('User_out/',views.user_logout,name='user_logout'),
    path('Profile/',views.profile,name='Profile'),
    path('old_password/',views.old_password,name='old_password'),
    path('old_password2/',views.old_password2,name='old_password2'),
    
]
