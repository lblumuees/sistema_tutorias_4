class Docente:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.tutorias = []

    def publicar_horario(self, tutoria):
        print(f"{self.nombre} publicó la tutoría {tutoria.tema} en {tutoria.horario}")

    def aceptar_reserva(self, reserva):         
        reserva.confirmar() 
        print(f"{self.nombre} aceptó la reserva {reserva.id}")