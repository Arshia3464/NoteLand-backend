from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from api.views import register
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),

    path("auth/register/", register),
    path("auth/login/", TokenObtainPairView.as_view()),
]
