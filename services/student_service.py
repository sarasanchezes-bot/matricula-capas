# services/student_service.py — Capa de Negocio (Service)
#
# Responsabilidad de esta capa:
#   - Validar reglas de negocio (créditos, datos obligatorios)
#   - Orquestar la operación entre capas
#   - Delegar el guardado a la capa de datos (Repository)
#
# Lo que esta capa NO hace:
#   - NO recibe peticiones HTTP (eso es del Controller)
#   - NO guarda directamente en la base de datos (eso es del Repository)

from repositories.student_repository import StudentRepository

MIN_CREDITOS = 1
MAX_CREDITOS = 32


class StudentService:

    def __init__(self, repository=None):
        # Inyección de dependencias: permite pasar un repositorio falso en tests
        self.repository = repository if repository is not None else StudentRepository()

    def registrar(self, datos):
        nombre = datos.get("nombre")
        codigo = datos.get("codigo")
        creditos = datos.get("creditos")

        if not nombre or not str(nombre).strip():
            raise ValueError("El nombre del estudiante es obligatorio")

        if not codigo or not str(codigo).strip():
            raise ValueError("El código del estudiante es obligatorio")

        if creditos is None:
            raise ValueError("Los créditos son obligatorios")

        if not isinstance(creditos, (int, float)) or isinstance(creditos, bool):
            raise ValueError("Los créditos deben ser un valor numérico")

        if creditos < MIN_CREDITOS:
            raise ValueError(
                f"Los créditos deben ser al menos {MIN_CREDITOS}"
            )

        if creditos > MAX_CREDITOS:
            raise ValueError(
                f"Los créditos no pueden superar {MAX_CREDITOS}"
            )

        return self.repository.guardar(datos)
