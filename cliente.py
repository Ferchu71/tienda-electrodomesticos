class Cliente:
    def __init__(self, nombre, dni, telefono):
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} | DNI: {self.dni} | Tel: {self.telefono}"
