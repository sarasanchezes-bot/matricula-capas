# STUB temporal (lo hace Diego). Solo para que Sara pueda probar.
from repositories.student_repository import StudentRepository

class StudentService:
    def __init__(self):
        self.repository = StudentRepository()

    def registrar(self, datos):
        # Aquí irá la validación de créditos de Diego
        return self.repository.guardar(datos)