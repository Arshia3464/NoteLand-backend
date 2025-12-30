from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileAdminSerializer, ProfileSerializer


# Give all info of the logged in user
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile_details(request):
    # Try to get the profile, or create one if missing
    profile, created = Profile.objects.get_or_create(
        user=request.user,
        defaults={"role": "user", "subscription_type": "free"}
    )
    
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)

# User self-update
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_my_profile(request):
    serializer = ProfileSerializer(request.user.profile, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Admin updates another user's profile
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def admin_update_profile(request, user_id):
    if request.user.profile.role != 'admin':
        return Response({"detail": "Only admins allowed!"}, status=status.HTTP_403_FORBIDDEN)

    profile = get_object_or_404(Profile, user__id=user_id)
    serializer = ProfileAdminSerializer(profile, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_profiles(request):
    if request.user.profile.role != 'admin':
        return Response({"detail": "Only admins allowed!"}, status=status.HTTP_403_FORBIDDEN)
    

    profiles = Profile.objects.all()  # fetch all profiles
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)