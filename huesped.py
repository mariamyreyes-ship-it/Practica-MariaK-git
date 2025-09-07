class Huesped:
    def __init__(self, nombre, documento_identidad, telefono):
        self.nombre = nombre
        self.documento_identidad = documento_identidad
        self.telefono = telefono
    def __str__(self):
        return f'Huésped: {self.nombre}, ID: {self.documento_identidad}, Teléfono: {self.telefono}'