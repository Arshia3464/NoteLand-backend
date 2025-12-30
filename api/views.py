from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# REGISTER endpoint
@api_view(["POST"])
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"detail": "Username and password required"}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({"detail": "Username already exists"}, status=400)

    User.objects.create_user(username=username, password=password)
    return Response({"status": "user created"})


# LOGIN - sets JWT cookies
@api_view(["POST"])
def login_cookie_jwt(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(request, username=username, password=password)
    if not user:
        return Response({"detail": "Invalid credentials"}, status=400)

    refresh = RefreshToken.for_user(user)
    response = Response({"status": "logged in"})

    # HttpOnly cookies
    response.set_cookie(
        key="access_token",
        value=str(refresh.access_token),
        httponly=True,
        samesite="Lax",
    )
    response.set_cookie(
        key="refresh_token",
        value=str(refresh),
        httponly=True,
        samesite="Lax",
    )
    return response


# LOGOUT - clears cookies
@api_view(["POST"])
def logout_cookie_jwt(request):
    response = Response({"status": "logged out"})
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return response


# Example protected endpoint
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected_test(request):
    return Response({"status": f"Hello {request.user.username}, you are authenticated!"})
