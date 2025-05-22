from fecha import Fecha
from direccion import Direccion
from usuario import Usuario

fecha1 = Fecha(20, 3, 2004)
sFecha1 = str(fecha1)
print(sFecha1)
print()

dir1 = Direccion("Cra 64C", "#51-61", "Carlos E. Restrepo", "Medellín", "Bloque 90", "301")
sDir1 = str(dir1)
print(sDir1)
print()

user1 = Usuario("Maria José Saad Plata", 123456, fecha1, "Barrancabermeja", 3186933020, "msaad@unal.edu.co", dir1)
sUser1 = str(user1)
print(sUser1)