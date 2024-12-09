from django.urls import path
from catalog.apps import CatalogConfig

from . import views

app_name = 'catalog'

urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
]
