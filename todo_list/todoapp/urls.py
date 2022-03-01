from django.contrib import admin
from django.urls import path
from .views import home, user, add_todo


urlpatterns = [
    path('', home, name='home'),
    path('user/', user),
    path('add_todo/', add_todo),
]
