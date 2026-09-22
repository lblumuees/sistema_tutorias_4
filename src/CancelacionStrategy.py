from abc import ABC, abstractmethod

class CancelacionStrategy(ABC):
    @abstractmethod
    def cancelar(self, reserva):
        pass

class CancelacionNormal(CancelacionStrategy):
    def cancelar(self, reserva):
        reserva.estado = "Cancelada (normal)"

class CancelacionPrioritaria(CancelacionStrategy):
    def cancelar(self, reserva):
        reserva.estado = "Cancelada (prioritaria)"

class CancelacionGrupal(CancelacionStrategy):
    def cancelar(self, reserva):
        reserva.estado = "Cancelada (grupal)"
