
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home),
    path('del/<int:id>/',views.delet_data)
]