from django.urls import path
from .views import sellers_list

urlpatterns = [
    path('sellers/', sellers_list, name='sellers_list'),
]
