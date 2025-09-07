class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True
    def __str__(self):
        estado = 'Disponible' if self.disponible else 'Ocupada'
        return f'Habitación {self.numero} {self.tipo} - {estado} - ${self.precio}/ noche'