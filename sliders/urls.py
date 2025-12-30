from django.urls import path
from .views import add_slider, delete_slider, slider_update, slider_list

urlpatterns = [
    path("", slider_list),
    path("add/", add_slider),
    path("delete/<int:pk>/", delete_slider),
    path("update/<int:pk>/", slider_update )
]
