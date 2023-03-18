from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import User
from .forms import UserForm

class UserCreate(CreateView):
    model = User
    form_class = UserForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')
