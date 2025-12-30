from django.urls import path
from .views import product_list, create_product, product_detail, product_delete, product_update

urlpatterns = [
    path("", product_list),
    path("create/", create_product),
    path("<int:pk>/", product_detail),
    path("delete/<int:pk>/", product_delete),
    path("update/<int:pk>/", product_update )
]
