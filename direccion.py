class Direccion:
    def __init__(self, calle=None, nomenclatura=None, barrio=None, ciudad=None, edificio=None, apto=None):
        self.calle = calle
        self.nomenclatura = nomenclatura
        self.barrio = barrio
        self.ciudad = ciudad
        self.edificio = edificio
        self.apto = apto

    def get_calle(self):
        return self.calle

    def set_calle(self, calle):
        self.calle = calle

    def get_nomenclatura(self):
        return self.nomenclatura

    def set_nomenclatura(self, nomenclatura):
        self.nomenclatura = nomenclatura

    def get_barrio(self):
        return self.barrio

    def set_barrio(self, barrio):
        self.barrio = barrio

    def get_ciudad(self):
        return self.ciudad

    def set_ciudad(self, ciudad):
        self.ciudad = ciudad

    def get_edificio(self):
        return self.edificio

    def set_edificio(self, edificio):
        self.edificio = edificio

    def get_apto(self):
        return self.apto

    def set_apto(self, apto):
        self.apto = apto

    def __str__(self):
        return f"{self.calle} {self.nomenclatura}, {self.edificio}, Apto: {self.apto}, Barrio: {self.barrio}, Ciudad: {self.ciudad}"