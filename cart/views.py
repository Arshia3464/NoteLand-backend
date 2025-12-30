from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Cart, CartItem
from products.models import Product
from .serializers import CartSerializer, CartItemSerializer

# Get or create cart for user
def get_user_cart(user):
    cart, created = Cart.objects.get_or_create(user=user)
    return cart

# List all items in cart
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def cart_detail(request):
    cart = get_user_cart(request.user)
    serializer = CartSerializer(cart)
    return Response(serializer.data)

# Add product to cart
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    product_id = request.data.get("product_id")
    quantity = request.data.get("quantity", 1)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"detail": "Product not found"}, status=404)

    cart = get_user_cart(request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += int(quantity)
        cart_item.save()
    else:
        cart_item.quantity = int(quantity)
        cart_item.save()

    serializer = CartSerializer(cart)
    return Response(serializer.data)

# Remove product from cart
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_from_cart(request):
    product_id = request.data.get("product_id")
    cart = get_user_cart(request.user)

    try:
        cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
        cart_item.delete()
    except CartItem.DoesNotExist:
        return Response({"detail": "Item not in cart"}, status=404)

    serializer = CartSerializer(cart)
    return Response(serializer.data)
