from src.CancelacionStrategy import CancelacionNormal, CancelacionPrioritaria, CancelacionGrupal
from src.Notificador import NotificadorCorreo
from src.Reserva import Reserva

class ServicioReservas:
    def __init__(self, estrategia, notificador):
        self.estrategia = estrategia
        self.notificador = notificador

    def crear_reserva(self, estudiante, tutoria, fecha):
        if not tutoria.disponible:
            return None
        
        reserva = self._crear_reserva_objeto(estudiante, tutoria, fecha)
        NotificadorReserva(self.notificador).notificar_creacion(estudiante)
        print(f"Tutoría {tutoria.materia} asignada a reserva {reserva.id}")
        return reserva

    def _validar_disponibilidad(self, tutoria):
        return tutoria.evaluar_disponibilidad()

    def _crear_reserva_objeto(self, estudiante, tutoria, fecha):
        reserva = Reserva(id=1, estudiante=estudiante, tutoria=tutoria, fecha=fecha)
        tutoria.asignar_reserva(reserva)
        return reserva

    def procesar_reserva(self, reserva):
        reserva.confirmar()
        NotificadorReserva(self.notificador).notificar_procesamiento()
        
    def cancelar_reserva(self, reserva):
        self.estrategia.cancelar(reserva)


class NotificadorReserva:
    def __init__(self, notificador):
        self.notificador = notificador

    def notificar_creacion(self, estudiante):
        self._notificar(estudiante.email, "Reserva creada exitosamente")

    def notificar_procesamiento(self):
        self._notificar(None, "Reserva procesada correctamente")

    def _notificar(self, destinatario, mensaje):
        self.notificador.destinatario = destinatario
        self.notificador.mensaje = mensaje
        self.notificador.enviar_mensaje()
