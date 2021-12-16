from django.urls import include, path
from rest_framework import routers
from local_apps.historia_clinica.views.evoluciones_views import EvolucionesViewSet
from local_apps.historia_clinica.views.usuario_views import UsuarioViewSet
from local_apps.historia_clinica.views.procedimiento_views import ProcedimientoViewSet
from local_apps.historia_clinica.views.paciente_views import PacienteViewSet

router = routers.DefaultRouter()
router.register(r"evoluciones", EvolucionesViewSet)
router.register(r"usuarios", UsuarioViewSet)
router.register(r"procedimientos", ProcedimientoViewSet)
router.register(r"pacientes", PacienteViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
