"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app import views
from django.contrib.auth import views as auth

urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),

    path('',include('app.urls')),
    path('index/',views.index,name = 'index'),
    path('login/',views.login_view, name = 'login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.register,name='register'),
    path('blood_types/',views.blood_types,name="blood_types"),
    path('blood_stocks',views.blood_stocks,name="blood_stocks"),
    path('blood_donor',views.blood_donor,name="blood_donor"),
    path('need_blood',views.need_blood,name="need_blood"),

    path('a_plus',views.a_plus,name='a_plus'),
    path('a_minus',views.a_minus,name='a_minus'),
    path('b_plus',views.b_plus,name='b_plus'),
    path('b_minus',views.b_minus,name='b_minus'),
    path('ab_plus',views.ab_plus,name='ab_plus'),
    path('ab_minus',views.ab_minus,name='ab_minus'),
    path('o_plus',views.o_plus,name='o_plus'),
    path('o_minus',views.o_minus,name='o_minus'),

    path('eml',views.eml,name="eml"),
    path('donor_mail',views.d_mail,name='donor_mail'),

]
    # path('login/',user_view.login,name='login'),
