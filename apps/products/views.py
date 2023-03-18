from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import transaction

from .models import Product
from .forms import ProductForm

class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'createProduct.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            
            return super().post(request, *args, **kwargs)
        
class ProductList(ListView):
    model = Product
    form_class = ProductForm
    template_name = 'home.html'
    success_url = reverse_lazy('home')