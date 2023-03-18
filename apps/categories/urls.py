from django.urls import path

from .views import CategoryCreate, CategoryDelete, CategoryDetail, CategoryUpdate, CategoryList

urlpatterns = [
    path('create/', CategoryCreate.as_view()),
    path('list/', CategoryList.as_view()),
    path('detail/', CategoryDetail.as_view()),
    path('update/', CategoryUpdate.as_view()),
    path('delete/', CategoryDelete.as_view()),
]

