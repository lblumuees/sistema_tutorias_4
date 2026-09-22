from Estudiante import Estudiante
from Docente import Docente
from Tutoria import Tutoria
from Reserva import Reserva
from Notificador import Notificador, NotificadorCorreo, NotificadorCalendario, NotificadorPanel
from CancelacionStrategy import CancelacionNormal, CancelacionPrioritaria, CancelacionGrupal
from ServicioReservas import ServicioReservas
from datetime import datetime

def main():
    # objetos base
    estudiante = Estudiante(1, "Luis", "luis@mail.com")
    docente = Docente(1, "Prof. Jaime")
    tutoria = Tutoria(1, "Diseño de Software", "08:00 PM", docente)

    # nueva reserva
    reserva = Reserva(1, estudiante, tutoria,"08/09/2026")

    # agregar observadores (Observer)
    reserva.agregar_observador(NotificadorCorreo())
    reserva.agregar_observador(NotificadorCalendario())
    reserva.agregar_observador(NotificadorPanel())

    # cambio de estado de la reserva (Observer)
    print("\n--- Cambio de estado de la reserva ---")
    reserva.cambiar_estado("Confirmada")

    # aplicar diferentes formas de cancelación (Strategy)
    print("\n--- Cancelación con estrategia normal ---")
    servicio_normal = ServicioReservas(CancelacionNormal())
    servicio_normal.cancelar_reserva(reserva)
    print(f"Estado actual: {reserva.estado}")

    print("\n--- Cancelación con estrategia prioritaria ---")
    servicio_prioritaria = ServicioReservas(CancelacionPrioritaria())
    servicio_prioritaria.cancelar_reserva(reserva)
    print(f"Estado actual: {reserva.estado}")

    print("\n--- Cancelación con estrategia grupal ---")
    servicio_grupal = ServicioReservas(CancelacionGrupal())
    servicio_grupal.cancelar_reserva(reserva)
    print(f"Estado actual: {reserva.estado}")

if __name__ == "__main__":
    main()
