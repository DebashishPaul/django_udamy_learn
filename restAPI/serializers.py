from rest_framework import serializers
from .models import MovieData

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieData
        fields = ['id', 'name', 'duration', 'rating', 'typ']