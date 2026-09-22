class Correo:
    def __init__(self, valor: str):
        if valor is None or "@" not in valor:
            raise ValueError("Correo inválido")
        self.valor = valor

    def __str__(self):
        return self.valor


class Estudiante:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = Correo(email)   # Value Object

    def solicitar_tutoria(self, tutoria):
        print(f"{self.nombre} solicita la tutoría {tutoria.tema}")

    def cancelar_reserva(self, reserva):
        reserva.cancelar()
        print(f"{self.nombre} canceló la reserva {reserva.id}")
