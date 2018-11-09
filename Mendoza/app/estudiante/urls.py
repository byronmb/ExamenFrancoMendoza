from django.urls import path

from . import views


urlpatterns = [
    path('', views.principal),
    path('crear', views.crear),
    path('modificar', views.modificar),
 #   path('eliminar', views.eliminar)
]