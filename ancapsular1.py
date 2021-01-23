class Alumno:
    def __init__(self, nombre, apellido):
        self.__nombre=nombre
        self.__apellido=apellido

    @property
    def nombreLista(self):
        return self.__nombre+" "+ self.__apellido

    @nombreLista.setter
    def nombreLista(self, nombreCompleto):
        self.__nombre, self.__apellido = nombreCompleto.split(' ')

alumno1 = Alumno("Eduardo", "Serey")

print(alumno1.nombreLista)
alumno1.nombreLista = "Juan Prerez"

print(alumno1.nombreLista)

print(alumno1.nombreLista)