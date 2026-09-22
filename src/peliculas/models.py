from django.db import models


class Pelicula(models.Model):
    titulo = models.CharField(max_length=150)
    genero = models.CharField(max_length=100)
    anio = models.IntegerField()
    duracion = models.IntegerField()
    puntuacion = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.titulo


class Resenia(models.Model):
    autor = models.CharField(max_length=100)
    comentario = models.TextField()
    puntuacion = models.IntegerField()

    pelicula = models.ForeignKey(
        Pelicula,
        on_delete=models.CASCADE,
        related_name="resenias",
    )

    def __str__(self):
        return f"{self.autor} - {self.pelicula.titulo}"