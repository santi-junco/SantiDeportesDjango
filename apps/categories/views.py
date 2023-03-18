from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from django.urls import reverse_lazy

from .models import Category
from .forms import CategoryForm

class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'createCategory.html'
    success_url = reverse_lazy('home')

class CategoryList(ListView):
    model = Category
    form_class = CategoryForm
    template_name = 'createCategory.html'
    success_url = reverse_lazy('home')

class CategoryDetail(DetailView):
    model = Category
    form_class = CategoryForm
    template_name = 'createCategory.html'
    success_url = reverse_lazy('home')

class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'createCategory.html'
    success_url = reverse_lazy('home')

class CategoryDelete(DeleteView):
    model = Category
    form_class = CategoryForm
    template_name = 'createCategory.html'
    success_url = reverse_lazy('home')
