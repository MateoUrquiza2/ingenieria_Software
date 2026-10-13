from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Pelicula, Resenia
from .serializers import (
    PeliculaSerializer,
    ReseniaPublicSerializer,
)


class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ReseniaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Resenia.objects.all().select_related("pelicula")
    serializer_class = ReseniaPublicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]