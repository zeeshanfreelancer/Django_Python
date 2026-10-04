import json 
from django.http import JsonResponse
from .models import Product

# GET — Get all products
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

# GET One Product
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

# POST — Create Product
def create_product(request):

    if request.method == "POST":

        data = json.loads(request.body)

        product = Product.objects.create(
            name=data["name"],
            price=data["price"],
            quantity=data["quantity"],
            description=data["description"]
        )

        return JsonResponse({
            "message": "Product created successfully",
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity,
            "description": product.description
        }, status=201)

# PUT — Update Product
def update_product(request, id):

    if request.method == "PUT":

        try:
            product = Product.objects.get(id=id)

        except Product.DoesNotExist:

            return JsonResponse({
                "error": "Product not found"
            }, status=404)

        data = json.loads(request.body)

        product.name = data["name"]
        product.price = data["price"]
        product.quantity = data["quantity"]
        product.description = data["description"]

        product.save()

        return JsonResponse({
            "message": "Product updated successfully"
        })

# DELETE — Delete Product
def delete_product(request, id):

    if request.method == "DELETE":

        try:
            product = Product.objects.get(id=id)

        except Product.DoesNotExist:

            return JsonResponse({
                "error": "Product not found"
            }, status=404)

        product.delete()

        return JsonResponse({
            "message": "Product deleted successfully"
        })