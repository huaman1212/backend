from fastapi import APIRouter
from ..services.estudiante_service import EstudianteServicio
from ..schemas.estudiante import Estudiante

from ..schemas.estudiante import Estudiante

rutasEstudiantes = APIRouter (prefix='/estudiantes', tags=['Estudiante'])

estudianteServicio = EstudianteServicio()

@rutasEstudiantes.post('/')
def guardarEstudiante(estudianteNuevo):
    return estudianteServicio.guardadEstudiante(estudianteNuevo)
@rutasEstudiantes.get ('/')
def mostrarEstudiante():
    return estudianteServicio.mostrarEstudiante()

@rutasEstudiantes.put('/{id}')
def actualizarEstudiante(id: int, estudianteActualizar:Estudiante):
    return estudianteServicio.actualizarEstudiante(id, estudianteActualizar)
    
@rutasEstudiantes.delete('/{id}')
def aliminarEstudiante(id: int):
    return estudianteServicio.eliminarEstudiante(id)
