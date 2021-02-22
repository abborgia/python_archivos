class Usuarios:
    def __init__(self, nid, alias, nombre, apellido, password):
        self.nid = nid
        self.alias = alias
        self.nombre = nombre
        self.apellido = apellido
        self.__password = password

    def muestra_datos(self):
        print("El nombre y el apellido son: {} {}".format(self.nombre, self.apellido))
        print("El ID del usuario es: {}".format(self.nid))
        print("El alias del usuario es: {}".format(self.alias))
        print("El pass del usuario es: {}".format(self.__password))

    def cambiarPass(self):
        passAnterior = input("Ingrese su pass actual:  >")
        if passAnterior == self.__password:
            print("Correcto... ya puedes cambiar tu contraseña")
            newPass=input("ingrese nueva contraseña: > ")
            print("Contraseña anterior %s" %self.__password)
            self.__password = newPass
            print("Contraseña nueva %s" %self.__password)


ususario1=Usuarios("001","abborgia","Eduardo","Serey","123456")
print(ususario1._Usuarios__password)

ususario1.muestra_datos()
ususario1.cambiarPass()
ususario1.muestra_datos()

