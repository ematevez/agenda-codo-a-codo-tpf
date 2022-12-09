from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  
  path('', views.index, name='todo'),
  path('view/<int:id>', views.views, name='todo_views'),
  path('edit/<int:id>', views.edit, name='todo_edit'),
  path('create/', views.create, name='todo_create'),
  path('delete/<int:id>', views.delete, name='todo_delete'),

]
