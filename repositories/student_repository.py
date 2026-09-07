# repositories/student_repository.py
#
# Capa de acceso a datos (Repository)
#
# Responsabilidad:
#   - Guardar estudiantes.
#   - Simular la persistencia en una base de datos.
#
# Esta capa NO contiene reglas de negocio.
# Las validaciones pertenecen a StudentService.


class StudentRepository:

    def __init__(self):
        # Simulación de una base de datos en memoria
        self.estudiantes = []

    def guardar(self, estudiante):
        """
        Guarda un estudiante en la base de datos simulada.

        Args:
            estudiante (dict): Datos del estudiante.

        Returns:
            dict: El estudiante guardado.
        """
        self.estudiantes.append(estudiante)
        return estudiante
