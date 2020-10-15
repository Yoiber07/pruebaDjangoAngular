from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import DirectorSerializer, PeliculaSerializer, PeliculaDirectorSerializer
from .models import Director, Pelicula

# Create your views here.


class DirectorLista(APIView):

    def get(self, request):
        director = Director.objects.all()
        serializer = DirectorSerializer(director, many=True)
        return Response(serializer.data)


class DirectorBuscar(APIView):

    def get(self, request, pk):
        idDirector = Director.objects.filter(pk=pk)
        serializer = DirectorSerializer(idDirector, many=True)
        return Response(serializer.data)


class DirectorRegistrar(APIView):
    def post(self, request):
        director = Director.objects.all()
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.error)


class DirectorEditar(APIView):
    def put(self, request, id):
        director = Director.objects.get(id=id)
        serializer = DirectorSerializer(director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)


class DirectorEliminar(APIView):
    def delete(self, request, id):
        director = Director.objects.get(id=id)
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PeliculaConDirector(APIView):
    def get(self, request):
        peliculas = Pelicula.objects.all()
        serializer = PeliculaDirectorSerializer(peliculas, many=True)
        return Response(serializer.data)


class PeliculaRegistrar(APIView):
    def post(self, request):

        pelicula = Pelicula.objects.all()
        serializer = PeliculaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.error)

class PeliculaBuscar(APIView):
    def get(self,request,id):
        peliculas = Pelicula.objects.get(id=id)
        serializer = PeliculaSerializer(peliculas, many=True)
        return Response(serializer.data)

class PeliculaEditar(APIView):
    def put(self,request,id):
        peliculas = Pelicula.objects.get(id=id)
        serializer =  PeliculaSerializer(peliculas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)


class PeliculaEliminar(APIView):
    def delete(self,request, id):
        peliculas = Pelicula.objects.filter(id=id)
        if peliculas:
            peliculas.delete()
            content = {'message': 'Elimnado'}
            return Response(content, status=status.HTTP_200_OK)
        else:
            content = {'message': 'No existe este usuario'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)


