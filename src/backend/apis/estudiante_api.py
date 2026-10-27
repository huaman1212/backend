from fastapi import APIRouter , HTTPException, status
from ..services.estudiante_service import EstudianteServicio
from ..schemas.estudiante import Estudiante

from ..schemas.estudiante import Estudiante

rutasEstudiantes = APIRouter (prefix='/estudiantes', tags=['Estudiante'])

estudianteServicio = EstudianteServicio()

@rutasEstudiantes.post('/')
def guardarEstudiante(estudianteNuevo):
    try:
        return estudianteServicio.guardadEstudiante(estudianteNuevo)
    except Exception as e :
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR  ,detail= str(e))
@rutasEstudiantes.get ('/')
def mostrarEstudiante():
    return estudianteServicio.mostrarEstudiante()

@rutasEstudiantes.put('/{id}')
def actualizarEstudiante(id: int, estudianteActualizar:Estudiante):
    try:
        return estudianteServicio.actualizarEstudiante(id, estudianteActualizar)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=(e))
@rutasEstudiantes.delete('/{id}')
def aliminarEstudiante(id: int):
    try:
        return estudianteServicio.eliminarEstudiante(id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))