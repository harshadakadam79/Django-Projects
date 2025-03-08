from django.contrib import admin
from django.urls import path
from myapp import views
from .views import get_user, create_user, update_user, delete_user

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('users/', get_user, name='get_user'),
    path('users/create/', create_user, name='create_user'),
     path('users/update/<int:user_id>/', update_user, name='update_user'),
    path('users/delete/<int:user_id>/', delete_user, name='delete_user'),

]
