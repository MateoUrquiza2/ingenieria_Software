from django.urls import path

from .views import (
    PeliculasListCreateAPIView,
    PeliculasDetailAPIView,
    ReseniasListCreateAPIView,
    ReseniasDetailAPIView,
)


urlpatterns = [
    path(
        "peliculas/",
        PeliculasListCreateAPIView.as_view(),
        name="peliculas_api",
    ),
    path(
        "peliculas/<int:pk>/",
        PeliculasDetailAPIView.as_view(),
        name="pelicula_detail_api",
    ),
    path(
        "resenias/",
        ReseniasListCreateAPIView.as_view(),
        name="resenias_api",
    ),
    path(
        "resenias/<int:pk>/",
        ReseniasDetailAPIView.as_view(),
        name="resenia_detail_api",
    ),
]