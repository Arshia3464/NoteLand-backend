from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order, OrderItem
from cart.models import Cart, CartItem
from products.models import Product


# ------------------------------
# Checkout: convert cart → order
# ------------------------------
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def checkout(request):
    user = request.user

    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        return Response({"detail": "Cart not found"}, status=404)

    cart_items = CartItem.objects.filter(cart=cart)
    if not cart_items.exists():
        return Response({"detail": "Cart is empty"}, status=400)

    # Create order
    order = Order.objects.create(user=user)
    total = 0

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )
        total += item.quantity * item.product.price

    order.total_price = total
    order.save()

    # Clear the cart
    cart_items.delete()

    return Response({"detail": "Order created", "order_id": order.id})


# ------------------------------
# List all orders for the user
# ------------------------------
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def my_orders(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    data = []

    for order in orders:
        items = [{
            "product": i.product.name if i.product else None,
            "quantity": i.quantity,
            "price": i.price
        } for i in order.items.all()]

        data.append({
            "id": order.id,
            "total_price": order.total_price,
            "status": order.status,
            "created_at": order.created_at,
            "items": items
        })

    return Response(data)


# ------------------------------
# Get single order by ID (optional)
# ------------------------------
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def order_detail(request, order_id):
    user = request.user
    try:
        order = Order.objects.get(id=order_id, user=user)
    except Order.DoesNotExist:
        return Response({"detail": "Order not found"}, status=404)

    items = [{
        "product": i.product.name if i.product else None,
        "quantity": i.quantity,
        "price": i.price
    } for i in order.items.all()]

    data = {
        "id": order.id,
        "total_price": order.total_price,
        "status": order.status,
        "created_at": order.created_at,
        "items": items
    }

    return Response(data)
