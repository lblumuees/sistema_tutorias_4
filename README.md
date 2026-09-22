# Sistema de Tutorías – Semana 5 (Refactorización)

En esta nueva etapa del sistema, se realizaron tests y análisis sobre refactorización, especialmente de la clase ServicioReservas.


## Estructura del repositorio

```
sistema_tutorias_3/
+-- src/          # Código fuente en Python
¦    +-- CancelacionStrategy.py
¦    +-- Docente.py
¦    +-- Estudiante.py
¦    +-- Notificador.py
¦    +-- Reserva.py
¦    +-- ServicioReservas.py
¦    +-- Tutoria.py
¦    +-- main.py
+-- tests/          # Código fuente en Python
¦    +-- test_servicio_reservas.py
+-- docs/         # Diagramas UML 
+-- README.md     # Descripción del proyecto
+-- .gitignore    # Archivos a excluir del control de versiones
```

## Cambios refactorización

- **Code Smells**:  
  - `ServicioReservas.crear_reserva` - Método con demasiadas responsabilidades  
  - `ServicioReservas (uso de notificador)` - La clase depende directamente de la implementación concreta del notificador
  

## Tecnologías

- Python 3.14.3  
- Git + GitHub  
- UML para diseño y documentación  
- Librería unittest para pruebas


