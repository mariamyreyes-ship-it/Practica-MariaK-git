class Reserva:
    def __init__(self, habitación, huesped, fecha_entrada, fecha_salida):
        self.habitación = habitación
        self.huesped = huesped
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.habitación.disponible = False
    
    def __str__(self):
        return (f'Reserva de {self.huesped.nombre} en la {self.habitacion.tipo}'
                f'número {self.habitación.número} desde {self.fecha_entrada}'
                f'hasta {self.fecha_salida}'
        )