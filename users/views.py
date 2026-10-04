import json 
from django.http import JsonResponse
from .models import Product

def products(request):
    if request.method == "GET":
        products = Product.objects.all()

        data = []

        for product in products:
            data.append({
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "quantity": product.quantity,
                "description": product.description
            })

        return JsonResponse(data, safe=False)

def product_detail(request, id):

    try:
        product = Product.objects.get(id=id)

        return JsonResponse({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity,
            "description": product.description
        })
    
    except Product.DoesNotExist:

        return JsonResponse({
            "error": "Product not found"
        }, status=404)