
from raton import *
computadora1=computadora("Electrónico","ADMINISTRADOR-P","HP","Azul")
print("Tipo de DNI",computadora1.DNI)
print("Nombre de la computadora:",computadora1.Nombre)
print("Marca de la computadora:",computadora1.Marca)
print("Color de la computadora:",computadora1.Color)
computadora1.encender()
computadora1.apagar()

monitor1=monitor("Tactil","Ryzen 5")
print("El tipo del monitor es:",monitor1.Tipo)
print("El modelo del monitor es:",monitor1.Modelo)


raton1=raton("PS/2","inalambrico",)
print("El tipo de entrada del raton es:",raton1.Tipo_entrada)
print("La conexion del raton es:",raton1.conexion)
raton1.conectar()
raton1.desconectar()



