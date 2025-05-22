from fecha import Fecha
from direccion import Direccion

class Usuario:
    def __init__(self, nombre=None, id=None, fecha_nacimiento=None, ciudad_nacimiento=None, tel=None, email=None, dir=None):
        self.nombre = nombre
        self.id = id
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.tel = tel
        self.email = email
        self.dir = dir

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def get_ciudad_nacimiento(self):
        return self.ciudad_nacimiento

    def set_ciudad_nacimiento(self, ciudad_nacimiento):
        self.ciudad_nacimiento = ciudad_nacimiento

    def get_tel(self):
        return self.tel

    def set_tel(self, tel):
        self.tel = tel

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_dir(self):
        return self.dir

    def set_dir(self, dir):
        self.dir = dir

    def __str__(self):
        return f"Usuario: Nombre: {self.nombre}\nID: {self.id}\nFecha nacimiento: {self.fecha_nacimiento}\nCiudad nacimiento: {self.ciudad_nacimiento}\nTel: {self.tel}\nCorreo: {self.email}\nDirección: {self.dir}"