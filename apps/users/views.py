from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import transaction

from apps.core.email import sendMail

from .models import Usuario
from .forms import UserForm

class UserCreate(CreateView):
    model = Usuario
    form_class = UserForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        with transaction.atomic():
            response = super().form_valid(form)
            user = self.object
            url = f'127.0.0.1:8000/users/verification/{user.id}/'
            sendMail('registro', 'Registro Exitoso', user.email, url)
            
            return response

