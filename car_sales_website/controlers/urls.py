<<<<<<< HEAD
from django.urls import path
from .import views
urlpatterns = [
    path('signup/',views.Register, name='signup'),
    path('login/',views.userLoginView.as_view(), name='login'),
    path('logout/',views.userLogoutView.as_view(), name='logout'),
    path('profile/',views.profile, name='profile'),
    path('buynow/<int:id>',views.Buy_now, name='buyNow'),
    path('user_data/',views.change_user_data, name='user_data'),
    path('details/<int:id>',views.DetailPostView.as_view(), name='details'),
=======
from django.urls import path
from .import views
urlpatterns = [
    path('signup/',views.Register, name='signup'),
    path('login/',views.userLoginView.as_view(), name='login'),
    path('logout/',views.userLogoutView.as_view(), name='logout'),
    path('profile/',views.profile, name='profile'),
    path('buynow/<int:id>',views.Buy_now, name='buyNow'),
    path('user_data/',views.change_user_data, name='user_data'),
    path('details/<int:id>',views.DetailPostView.as_view(), name='details'),
>>>>>>> 1536a79ed4bb132d457adca7cd486953d8e04534
]