from rest_framework import serializers
from .models import BrandModel

class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = ['name','year','followers','desc']