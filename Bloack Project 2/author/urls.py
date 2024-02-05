from django.urls import path
from .import views
urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/',views.user_login, name='user_login'),
    path('profile/',views.Profile, name='profile'),
    path('Change_pass/',views.Passchnagen, name='passCh'),
    path('logout/',views.User_logout, name='User_logout'),
    path('profile/edit',views.edit_profile, name='edit_profile'),
]
