# Sistema de Tutorías – Semana 6 (Refactorización respaldada por pruebas unitarias)

En esta nueva etapa del sistema, se realizaron refactorizaciones justificadas de mayor alcance.


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

## Conclusiones cambios refactorización

- Las refactorizaciones aplicadas lograron separar responsabilidades y asignarlas a las clases correctas, lo que incrementa la claridad y mantenibilidad del sistema.
- La cohesión mejoró porque cada clase ahora concentra métodos relacionados con su propósito (reservas, notificación, disponibilidad, validación de correo).
- El acoplamiento se redujo al delegar tareas específicas a nuevas clases (NotificadorReserva, Correo) y mover métodos a donde pertenecen (Tutoria).
- Se fortaleció el modelo de dominio, introduciendo un Value Object para el correo, lo que garantiza datos más confiables y expresivos.
- Los condicionales se simplificaron al centralizar la lógica de disponibilidad en Tutoria.
- El uso de Git con commits pequeños y descriptivos dejó evidencia clara y trazable de cada refactorización, cumpliendo buenas prácticas de control de versiones. 



## Tecnologías

- Python 3.14.3  
- Git + GitHub  
- UML para diseño y documentación  
- Librería unittest para pruebas


