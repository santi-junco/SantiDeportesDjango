from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Usuario
from .forms import UserForm

class UserCreate(CreateView):
    model = Usuario
    form_class = UserForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')
