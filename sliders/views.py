from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Slider
from .serializers import SliderSerializer

# List all available sliders (public)
@api_view(["GET"])
def slider_list(request):
    sliders = Slider.objects.all()
    serializer = SliderSerializer(sliders, many=True)
    return Response(serializer.data)

# Create a slider (only logged-in users)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_slider(request):
    serializer = SliderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(publisher=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_slider(request, pk):
    try:
        slider = Slider.objects.get(pk=pk)
    except Slider.DoesNotExist:
        return Response({"detail": "Slider not found"}, status=404)
    slider.delete()
    return Response({"detail": "Product deleted"}, status=204)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def slider_update(request, pk):
    try:
        slider = Slider.objects.get(pk=pk)
    except Slider.DoesNotExist:
        return Response({"detail": "Not found"}, status=404)

    serializer = SliderSerializer(slider, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

