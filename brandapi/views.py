from django.shortcuts import render
from .models import BrandModel
from .serializers import BrandSerializers
from rest_framework import viewsets
# Create your views here.

class BrandViewSet(viewsets.ModelViewSet):
    queryset = BrandModel.objects.all()
    serializer_class = BrandSerializers