from django.urls import path
from .views import user_info, all_users

urlpatterns = [
    path("me/", user_info),
    path('', all_users)
]