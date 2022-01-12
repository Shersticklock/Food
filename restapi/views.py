from django.shortcuts import render
from .serializers import FoodSerializer, FoodListSerializer
from .models import FoodCategory, Food
from rest_framework import viewsets
from rest_framework.response import Response


class FoodView(viewsets.ViewSet):
    """
    A simple ViewSet that for listing or retrieving users.
    """
    def list(self, request):
        queryset = FoodCategory.objects.filter(food__is_publish=True)
        serializer = FoodListSerializer(queryset, many=True)
        return Response({"results": serializer.data})