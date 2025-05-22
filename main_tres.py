from agenda import Agenda
from usuario import Usuario
from fecha import Fecha
from direccion import Direccion

if __name__ == "__main__":
    agenda = Agenda()

    fecha1 = Fecha(22, 3, 1992)
    dir1 = Direccion("Avenida Siempre Viva", "742", "Springfield", "Ciudad Capital", "Casa Amarilla", "1A")
    user1 = Usuario("Homero J. Simpson", 12345678901, fecha1, "Springfield", 1122334455, "homer.simpson@outlook.com", dir1)

    fecha2 = Fecha(1, 1, 1980)
    dir2 = Direccion("Calle Falsa", "123", "Pueblo Paleta", "Kanto", "Laboratorio", "001")
    user2 = Usuario("Ash Ketchum", 98765432109, fecha2, "Pueblo Paleta", 9988776655, "ash.ketchum@gmail.com", dir2)

    fecha3 = Fecha(30, 11, 1995)
    dir3 = Direccion("Boulevard de los Sueños Rotos", "99", "Oaxaca", "Oaxaca", "Dream Palace", "303")
    user3 = Usuario("María Fernández", 56473829101, fecha3, "Oaxaca", 5544332211, "maria.fernandez@yahoo.com", dir3)

    fecha4 = Fecha(5, 7, 1988)
    dir4 = Direccion("Carrera 10", "20-15", "Centro", "Medellín", "Torre Central", "801")
    user4 = Usuario("Juan David Pérez", 23456789012, fecha4, "Medellín", 6677889900, "juan.perez@example.com", dir4)

    fecha5 = Fecha(10, 2, 2000)
    dir5 = Direccion("Vía Láctea", "1", "Espacio Exterior", "Universo", "Estación Espacial", "Alpha")
    user5 = Usuario("Zoe Galáctica", 87654321098, fecha5, "Desconocido", 1029384756, "zoe.galactic@galaxy.net", dir5)

    agenda.agregar(user1)
    agenda.agregar(user2)
    agenda.agregar(user3)
    agenda.agregar(user4)
    agenda.agregar(user5)

    agenda.mostrar()

    agenda.mostrar_usuario(user1.get_id())
    agenda.mostrar_usuario(user5.get_id())

    agenda.eliminar(user2.get_id())
    
    agenda.mostrar()