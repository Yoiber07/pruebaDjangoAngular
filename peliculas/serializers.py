from rest_framework import serializers
from .models import Pelicula, Director


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class PeliculaDirectorSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(read_only=True)
    class Meta:
        model = Pelicula
        fields = '__all__'


class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'
