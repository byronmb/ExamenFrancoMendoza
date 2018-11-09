from django import forms
from app.modelo.models import Estudiante

class FormularioEstudiante(forms.ModelForm):
    class Meta:
        model =Estudiante
        fields =["cedula", "nombre", "apellidos","genero", "matricula", "curso"]
