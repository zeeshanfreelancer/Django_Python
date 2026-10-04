from django.urls import path

from .views import (
    products,
    product_detail,
    create_product,
    update_product,
    delete_product
)

urlpatterns = [

    path("products/", products),

    path("products/create/", create_product),

    path("products/<int:id>/", product_detail),

    path("products/<int:id>/update/", update_product),

    path("products/<int:id>/delete/", delete_product),

]