from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('create_task', views.create_task, name='create_task'),
    path('view_task', views.view_task, name='view_task'),
    path('delete/<str:title>/', views.delete_task, name='delete'),
    path('mark_as_completed/<str:title>/', views.mark_as_completed, name='mark_as_completed'),
    path('update_task/<str:title>/', views.update_task, name='update_task'),
    path('register', views.register, name='register')
]

