from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User  # default Django User

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_info(request):
    user = request.user
    return Response({
        "username": user.username,
        "joined": user.date_joined,
        "last_login": user.last_login,
        # "email": user.email,
    })

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def all_users(request):
    users = User.objects.all()
    data = []
    for user in users:
        data.append({
            "username": user.username,
            "joined": user.date_joined,
            "last_login": user.last_login,
            # "email": user.email,
        })
    return Response(data)
