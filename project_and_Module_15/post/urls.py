from django.urls import path,include
from .import views
urlpatterns = [
    path('add/',views.add_post, name='add_post'),
    path('add/<int:id>',views.edit_post, name='edit_post'),
    path('delete/<int:id>',views.delete_post, name='delete_post'),
]
