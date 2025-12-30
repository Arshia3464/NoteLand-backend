from django.urls import path
from .views import cart_detail, add_to_cart, remove_from_cart

urlpatterns = [
    path("", cart_detail),
    path("add/", add_to_cart),
    path("remove/", remove_from_cart),
]
