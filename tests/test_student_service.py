# tests/test_student_service.py — Fase 3: Prueba de Fuego (Validación)
#
# Este test demuestra AISLAMIENTO DE CAPAS:
#   - Se inyecta un repositorio FALSO (Mock) al Service
#   - NO se necesita base de datos real para ejecutar
#   - Si este test falla sin conexión a BD, las capas están acopladas mal

import unittest
from unittest.mock import MagicMock
from services.student_service import StudentService


class TestStudentServiceIsolated(unittest.TestCase):
    """Test unitario con repositorio mockeado (sin base de datos)."""

    def setUp(self):
        # Crear un repositorio falso (Mock)
        self.mock_repository = MagicMock()
        # Inyectarlo al Service en lugar del repositorio real
        self.service = StudentService(repository=self.mock_repository)

    # ── Caso exitoso ──

    def test_registrar_estudiante_valido(self):
        """Un estudiante con datos completos se registra correctamente."""
        datos = {"nombre": "Diego Robles", "codigo": "20231001", "creditos": 18}
        self.mock_repository.guardar.return_value = datos

        resultado = self.service.registrar(datos)

        self.mock_repository.guardar.assert_called_once_with(datos)
        self.assertEqual(resultado, datos)

    # ── Validación de créditos ──

    def test_creditos_menores_al_minimo_lanza_error(self):
        """Créditos por debajo del mínimo deben ser rechazados."""
        datos = {"nombre": "Sara Sanchez", "codigo": "20231002", "creditos": 0}

        with self.assertRaises(ValueError) as ctx:
            self.service.registrar(datos)

        self.assertIn("al menos", str(ctx.exception))
        self.mock_repository.guardar.assert_not_called()

    def test_creditos_mayores_al_maximo_lanza_error(self):
        """Créditos por encima del máximo deben ser rechazados."""
        datos = {"nombre": "Juliana Lopez", "codigo": "20231003", "creditos": 50}

        with self.assertRaises(ValueError) as ctx:
            self.service.registrar(datos)

        self.assertIn("superar", str(ctx.exception))
        self.mock_repository.guardar.assert_not_called()

    def test_creditos_ausentes_lanza_error(self):
        """Si no se envían créditos, debe rechazarse."""
        datos = {"nombre": "Carlos Perez", "codigo": "20231004"}

        with self.assertRaises(ValueError) as ctx:
            self.service.registrar(datos)

        self.assertIn("obligatorio", str(ctx.exception))

    # ── Validación de datos obligatorios ──

    def test_nombre_vacio_lanza_error(self):
        """El nombre es obligatorio."""
        datos = {"nombre": "", "codigo": "20231005", "creditos": 15}

        with self.assertRaises(ValueError) as ctx:
            self.service.registrar(datos)

        self.assertIn("nombre", str(ctx.exception))
        self.mock_repository.guardar.assert_not_called()

    def test_codigo_ausente_lanza_error(self):
        """El código es obligatorio."""
        datos = {"nombre": "Ana Garcia", "creditos": 12}

        with self.assertRaises(ValueError) as ctx:
            self.service.registrar(datos)

        self.assertIn("código", str(ctx.exception))
        self.mock_repository.guardar.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
