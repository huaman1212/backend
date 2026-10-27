from ..schemas.estudiante import Estudianterepositorio
from ..schemas.estudiante import Estudiante

class EstudianteServicio:

    def __init__(self):
        self.__estudianteRepositorio = Estudianterepositorio()
    def guandarEstudiante(self, estudianteNuevo: Estudiante):
        return self.__estudianteRepositorio.guardarEstudiante(estudianteNuevo)
        
    def mostrarEsdudiante(self):
        return self.__estudianteRepositorio.mostrarEstudiantes()
    def actualizarEstudiante(self, id: int, estudianteActualizar: Estudiante):
        for indice ,  valor in enumerate(self.__listaEstudiantes):
            if valor.id == id: 
                valor.nombre = estudianteActualizar.nombre
                valor.edad = estudianteActualizar.edad
                valor.correo = estudianteActualizar.correo
                return valor
        return None
    
    
    def eliminarEstudiante(self):
        pass
        