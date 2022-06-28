class computadora:
    def __init__(self,DNI,Nombre,Marca,Color):
        self.DNI=DNI
        self.Nombre=Nombre
        self.Marca=Marca
        self.Color=Color

    def encender(self):
       print("La computadora",self.Nombre,"Esta encendida")
    def apagar(self):
        print("La computadora",self.Nombre,"Esta apagada")


