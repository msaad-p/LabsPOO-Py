from usuario import Usuario

class Agenda:
    def __init__(self, capacity):
        self.registro = [None] * capacity
        self.no_reg = 0

    def agregar(self, u):
        if self.buscar(u.get_id()) != -1:
            return False
        if self.no_reg < len(self.registro):
            self.registro[self.no_reg] = u
            self.no_reg += 1
            return True
        else:
            return False

    def buscar(self, id):
        for i in range(self.no_reg):
            if self.registro[i].get_id() == id:
                return i
        return -1

    def eliminar(self, id):
        posicion_a_eliminar = self.buscar(id)
        if posicion_a_eliminar == -1:
            return False
        else:
            for i in range(posicion_a_eliminar, self.no_reg - 1):
                self.registro[i] = self.registro[i + 1]
            self.registro[self.no_reg - 1] = None
            self.no_reg -= 1
            return True

    def mostrar(self):
        if self.no_reg == 0:
            print("La agenda está vacía.")
            return
        print("--- Usuarios registrados en la Agenda ---")
        for i in range(self.no_reg):
            print(f"Nombre: {self.registro[i].get_nombre()}")
            print(f"ID: {self.registro[i].get_id()}")

    def mostrar_usuario(self, id):
        posicion = self.buscar(id)

        if posicion != -1:
            user = self.registro[posicion]
            print("--- Información del Usuario ---")
            print(user)  # The __str__ method of Usuario is called automatically
        else:
            print(f"El usuario con ID {id} no se encontró en la agenda.")