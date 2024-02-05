<<<<<<< HEAD
from django.urls import path,include
from .import views
urlpatterns = [
    path('singup/',views.SignupForm.as_view(), name="signup"),
    path('login/',views.user_login.as_view(), name="login"),
    path('logout/',views.user_logout.as_view(), name="logout"),

=======
from django.urls import path,include
from .import views
urlpatterns = [
    path('singup/',views.SignupForm.as_view(), name="signup"),
    path('login/',views.user_login.as_view(), name="login"),
    path('logout/',views.user_logout.as_view(), name="logout"),

>>>>>>> 1536a79ed4bb132d457adca7cd486953d8e04534
]