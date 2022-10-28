from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarSolicitud/', views.registrarSolicitud),
    path('edicionSolicitud/<codigo>', views.edicionSolicitud),
    path('editarSolicitud/', views.editarSolicitud),
    path('eliminarSolicitud/<codigo>', views.eliminarSolicitud),
]