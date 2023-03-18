from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import UserCreate

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html')),
    path('logout/', LogoutView.as_view()),

    path('create/', UserCreate.as_view()),
]