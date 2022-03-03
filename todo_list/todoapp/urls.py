from django.contrib import admin
from django.urls import path
from .views import delete_task, home, add_todo, delete_task, update_task


urlpatterns = [
    path('', home, name='home'),
    path('add_todo/', add_todo),
    path('update_task/<str:id>/', update_task, name='update_task'),
    path('delete/<int:id>/', delete_task, name='delete_task')
]
