from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name ='login'),
    path('login_doc', views.login_doctor, name ='login_doc'),
    path('login_nurse', views.login_nurse, name ='login_nurse'),
    path('register_doctor', views.register_doctor, name ='regdoc'),
    path('register_nurse', views.register_nurse, name ='regnurse'),
    path('redirect', views.redirect, name ='redirect'),
    path('register', views.register, name ='register'),
    path('logout', views.logout_views, name ='logout'),
]
