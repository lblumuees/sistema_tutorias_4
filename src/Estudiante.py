class Estudiante:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

    def solicitar_tutoria(self, tutoria):
        print(f"{self.nombre} solicita la tutoría {tutoria.tema}")

    def cancelar_reserva(self, reserva):
        reserva.cancelar()
        print(f"{self.nombre} canceló la reserva {reserva.id}")