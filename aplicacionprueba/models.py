
class persona(object):
    def __init__(self):
        self.Nombre=''
        self.Apellido=''
    """description of class"""

    def guardar(self,nombre,apellido):
         archivo = open('persona.txt', 'w')
         archivo.write(nombre +' ' +apellido)
         archivo.close()