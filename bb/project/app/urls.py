from django.urls import path
from . import views

urlpatterns = [
    path('login/home.html', views.home, name ='home'),
    path('',views.home,name="home")
]