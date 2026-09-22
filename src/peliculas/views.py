from rest_framework import generics

from .models import Pelicula, Resenia
from .serializers import (
    PeliculaSerializer,
    ReseniaSerializer,
    ReseniaPublicSerializer,
)


class PeliculasListCreateAPIView(generics.ListCreateAPIView):
    name = "Peliculas API"
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer


class PeliculasDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    name = "Peliculas API"
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer


class ReseniasListCreateAPIView(generics.ListCreateAPIView):
    name = "Reseñas API"
    queryset = Resenia.objects.all().select_related("pelicula")

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReseniaPublicSerializer
        else:
            return ReseniaSerializer


class ReseniasDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    name = "Reseñas API"
    queryset = Resenia.objects.all().select_related("pelicula")

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReseniaPublicSerializer
        else:
            return ReseniaSerializer