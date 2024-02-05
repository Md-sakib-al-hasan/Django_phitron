from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/',views.register, name='register'),
    # path('login/',views.user_login, name='user_login'),
    path('login/',views.UserLoginView.as_view(), name='user_login'),
    path('profile/',views.Profile, name='profile'),
    # path('Change_pass/',views.Passchnagen, name='passCh'),
    path('logout/',views.UserLoginView.as_view() , name='User_logout'),
    path('profile/edit',views.edit_profile, name='edit_profile'),
]
