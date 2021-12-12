from django.urls import include, path
from rest_framework import routers
from local_apps.historia_clinica.views.evoluciones_views import EvolucionesViewSet

router = routers.DefaultRouter()
router.register(r"evoluciones", EvolucionesViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
