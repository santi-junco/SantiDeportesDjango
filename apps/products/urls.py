from django.urls import path

from .views import ProductCreate, ProductList

urlpattern = [
    path('create/',ProductCreate.as_view()),
    path('list/',ProductList.as_view()),
]