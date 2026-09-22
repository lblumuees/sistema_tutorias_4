from src.Estudiante import Estudiante
from src.Docente import Docente
from src.Tutoria import Tutoria
from src.Reserva import Reserva
from src.Notificador import Notificador, NotificadorCorreo, NotificadorCalendario, NotificadorPanel
from src.CancelacionStrategy import CancelacionNormal, CancelacionPrioritaria, CancelacionGrupal
from src.ServicioReservas import ServicioReservas
from datetime import datetime

def main():
    # objetos base
    estudiante = Estudiante(1, "Luis", "luis@mail.com")
    docente = Docente(1, "Prof. Jaime")
    #tutoria = Tutoria(1, "Diseño de Software", "08:00 PM", docente)
    tutoria = Tutoria("Diseño de Software")

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
    servicio_normal = ServicioReservas(CancelacionNormal(), NotificadorCalendario())
    servicio_normal.cancelar_reserva(reserva)
    print(f"Estado actual: {reserva.estado}")

    print("\n--- Cancelación con estrategia prioritaria ---")
    servicio_prioritaria = ServicioReservas(CancelacionPrioritaria(), NotificadorCalendario())
    servicio_prioritaria.cancelar_reserva(reserva)
    print(f"Estado actual: {reserva.estado}")

    print("\n--- Cancelación con estrategia grupal ---")
    servicio_grupal = ServicioReservas(CancelacionGrupal(), NotificadorCalendario())
    servicio_grupal.cancelar_reserva(reserva)
    print(f"Estado actual: {reserva.estado}")

if __name__ == "__main__":
    main()
