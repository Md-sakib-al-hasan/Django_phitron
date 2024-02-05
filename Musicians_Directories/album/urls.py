from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.album.as_view(), name="album"),
    path('de/<int:id>',views.delete_album.as_view(), name="delete_album"),
    path('edit/<int:id>',views.Edit_album.as_view(), name="edit_album"),
]