class Tutoria:
    def __init__(self, materia, disponible=True):
        self.materia = materia
        self.disponible = disponible
        self.reserva = None

    def asignar_reserva(self, reserva):
        self.reserva = reserva
        self.disponible = False

    def evaluar_disponibilidad(self):
        return self.disponible
            