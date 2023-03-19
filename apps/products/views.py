from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import transaction

from apps.core.exceptions import CustomException

from .models import Product, ProductCategory, ProductPhoto
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            products = Product.objects.filter(active=True)
        except Exception as e:
            print(e)
            raise CustomException("Error al obtener productos")
        
        listProd = []
        
        if products:
            for product in products:
                try:
                    photos = list(ProductPhoto.objects.filter(product=product).values_list('photo', flat=True))
                except:
                    photos = []

                dic_photo = {
                    'id': product.id,
                    'name': product.name,
                    'description': product.description,
                    'price': product.price,
                    'talle': product.talle,
                    'photo': photos
                }

                listProd.append(dic_photo)
        
        context['listProd'] = listProd
        return context