class Tutoria:
    def __init__(self, id, tema, horario, docente):
        self.id = id
        self.tema = tema
        self.horario = horario
        self.docente = docente
        self.reservada = False

    def evaluar_disponibilidad(self):
        return not self.reservada

    def asignar_reserva(self, reserva):
        if self.evaluar_disponibilidad():
            self.reservada = True
            print(f"Tutoría {self.tema} asignada a reserva {reserva.id}")
        else:
            print(f"Tutoría {self.tema} no disponible")