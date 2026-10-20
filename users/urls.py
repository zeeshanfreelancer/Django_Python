from django.urls import path
from .views import products_api, product_detail_api

urlpatterns = [
    path("products/", products_api),
    path("products/<int:id>/", product_detail_api),
]