from rest_framework import serializers

from .models import Pelicula, Resenia


class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = [
            "id",
            "titulo",
            "genero",
            "anio",
            "duracion",
            "puntuacion",
        ]
        read_only_fields = ["id"]


class ReseniaPublicSerializer(serializers.ModelSerializer):
    pelicula = PeliculaSerializer(read_only=True)

    class Meta:
        model = Resenia
        fields = [
            "id",
            "autor",
            "comentario",
            "puntuacion",
            "pelicula",
        ]
        read_only_fields = ["id"]


class ReseniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resenia
        fields = [
            "id",
            "autor",
            "comentario",
            "puntuacion",
            "pelicula",
        ]
        read_only_fields = ["id"]