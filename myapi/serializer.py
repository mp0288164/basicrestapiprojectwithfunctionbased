from rest_framework import serializers
from . models import MyApiModel

class MySerializer(serializers.ModelSerializer):
    class Meta:
        model=MyApiModel
        fields='__all__'