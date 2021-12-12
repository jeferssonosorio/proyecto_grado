from django.urls import include, path
from rest_framework import routers
from local_apps.historia_clinica.views.evoluciones_views import EvolucionesViewSet
from local_apps.historia_clinica.views.usuario_views import UsuarioViewSet

router = routers.DefaultRouter()
router.register(r"evoluciones", EvolucionesViewSet)
router.register(r"usuarios", UsuarioViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
