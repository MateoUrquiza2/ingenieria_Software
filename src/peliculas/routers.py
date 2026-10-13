from rest_framework.routers import DefaultRouter

from .views import PeliculaViewSet, ReseniaViewSet


router = DefaultRouter()

router.register(
    "peliculas",
    PeliculaViewSet,
    basename="peliculas",
)

router.register(
    "resenias",
    ReseniaViewSet,
    basename="resenias",
)

urlpatterns = router.urls