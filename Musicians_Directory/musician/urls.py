<<<<<<< HEAD
from django.urls import path
from .import views
urlpatterns = [
    path('add/',views.add_musician, name='musician'),
    path('edit/<int:id>',views.edit_musician, name='edit_musician'),
]
=======
from django.urls import path
from .import views
urlpatterns = [
    path('add/',views.add_musician, name='musician'),
    path('edit/<int:id>',views.edit_musician, name='edit_musician'),
]
>>>>>>> 1536a79ed4bb132d457adca7cd486953d8e04534
