from django.urls import path
from .views import checkout, my_orders

urlpatterns = [
    path("checkout/", checkout, name="checkout"),      # POST: create an order from cart
    path("my-orders/", my_orders, name="my_orders"),  # GET: list orders for logged-in user
]
