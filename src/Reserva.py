class Reserva:
    def __init__(self, id, estudiante, tutoria, fecha):
        self.id = id
        self.fecha = fecha
        self.estado = "Pendiente"
        self.estudiante = estudiante
        self.tutoria = tutoria
        self.observadores = []

    """
    def confirmar(self):
        self.estado = "Confirmada"
        print(f"Reserva {self.id} confirmada")

    def cancelar(self):
        self.estado = "Cancelada"
        print(f"Reserva {self.id} cancelada")
    """    
    
    def agregar_observador(self, obs):
        self.observadores.append(obs)

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        self.notificar_observadores()

    def notificar_observadores(self):
        for obs in self.observadores:
            obs.actualizar(self)