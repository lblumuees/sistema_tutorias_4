from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def actualizar(self, reserva):
        pass

class NotificadorCorreo(Notificador):
    def __init__(self):
        self.destinatario = None
        self.mensaje = None

    def enviar_mensaje(self):
        # Simulación de envío de correo
        print(f"Correo enviado a {self.destinatario}: {self.mensaje}")
    
    def actualizar(self, reserva):
        print(f"Correo enviado: Reserva {reserva.id} cambió a {reserva.estado}")

class NotificadorCalendario(Notificador):
    def actualizar(self, reserva):
        print(f"Calendario actualizado: Reserva {reserva.id} cambió a {reserva.estado}")

class NotificadorPanel(Notificador):
    def actualizar(self, reserva):
        print(f"Panel notificado: Reserva {reserva.id} cambió a {reserva.estado}")
