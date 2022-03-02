from django.contrib import admin
from django.urls import path
from .views import delete_task, home, user, add_todo, update_task, delete_task


urlpatterns = [
    path('', home, name='home'),
    path('user/', user),
    path('add_todo/', add_todo),
    path('add_todo/<int:id>/', add_todo, name='update_task'),
    path('delete/<int:id>/', delete_task, name='delete_task')
]
