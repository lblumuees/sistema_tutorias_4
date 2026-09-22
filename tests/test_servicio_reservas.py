import unittest
from src.ServicioReservas import ServicioReservas
from src.CancelacionStrategy import CancelacionNormal, CancelacionPrioritaria, CancelacionGrupal
from src.Notificador import NotificadorCorreo
from src.Estudiante import Estudiante
from src.Docente import Docente
from src.Tutoria import Tutoria
from src.Reserva import Reserva

class TestServicioReservas(unittest.TestCase):
    def setUp(self):
        self.notificador = NotificadorCorreo()
        self.servicio = ServicioReservas(CancelacionNormal(), self.notificador)
        self.estudiante = Estudiante(1,"Luis", "luis@email.com")        
        self.docente = Docente(1, "Prof. Jaime")
        self.tutoria = Tutoria(1, "Diseño de Software", "08:00 PM", self.docente)

    def test_crear_reserva_disponible(self):
        self.tutoria.disponible = True
        reserva = Reserva(1, self.estudiante, self.tutoria,"08/09/2026")
        self.assertIsNotNone(reserva)
        self.assertEqual(reserva.estudiante, self.estudiante)

    def test_crear_reserva_no_disponible(self):
        self.tutoria.disponible = False
        reserva = self.servicio.crear_reserva(self.estudiante, self.tutoria, "2026-09-15")
        self.assertIsNone(reserva)

    def test_cancelar_reserva_normal(self):
        reserva = Reserva(1, self.estudiante, self.tutoria, "2026-09-15")
        self.servicio.cancelar_reserva(reserva)
        self.assertEqual(reserva.estado, "Cancelada (normal)")

