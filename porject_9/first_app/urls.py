from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.home , name='home'),
    path('get/',views.session_get , name='cookie'),
    path('del/',views.session_delete , name='del'),
    path('se/',views.session_add , name='se'),
]
