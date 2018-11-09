from django.contrib import admin

# Register your models here.

from .models import Estudiante

class AdminEstudiante(admin.ModelAdmin):
    list_display = ["cedula","apellidos","nombre"]
    list_editable = ["apellidos", "nombre"]
    list_filter = ["apellidos","genero"]
    search_fields = ["cedula"],"apellidos","nombre"

    class Meta:               #HACEN EL VINCULO
        model = Estudiante

admin.site.register(Estudiante,AdminEstudiante)
