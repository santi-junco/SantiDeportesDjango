from django.urls import path

from .views import UserCreate

urlpattern = [
    path('create/', UserCreate.as_view()),
]