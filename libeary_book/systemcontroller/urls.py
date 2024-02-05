from django.urls import path
from .import views
urlpatterns = [
    path('signup/',views.Register, name='signup'),
    path('login/',views.userLoginView.as_view(), name='login'),
    path('logout/',views.userLogoutView.as_view(), name='logout'),
    path('details/<int:id>',views.DetailPostView.as_view(), name='details'),
    path('profile/',views.profile, name='profile'),
    path('deposits/',views.DepositListCreateView.as_view(), name='Deposit'),
]