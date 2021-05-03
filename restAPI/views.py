from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializers
from .models import MovieData
# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializers

class ActionTypeMovie(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='action')
    serializer_class = MovieSerializers

class ComedyTypeMovie(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='comedy')
    serializer_class = MovieSerializers