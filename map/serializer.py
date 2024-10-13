from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'titre', 'address', 'telephone', 'hours', 'gouvernorat', 'localite', 'type')
