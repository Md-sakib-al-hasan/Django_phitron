<<<<<<< HEAD
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.musician.as_view(), name="musician"),
    path('edit/<int:id>',views.Edit_musician.as_view(), name='edit_musician')
=======
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.musician.as_view(), name="musician"),
    path('edit/<int:id>',views.Edit_musician.as_view(), name='edit_musician')
>>>>>>> 1536a79ed4bb132d457adca7cd486953d8e04534
]