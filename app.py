# app.py — Capa de Presentación (Controller)
#
# Responsabilidad de esta capa:
#   - Recibir la petición HTTP del cliente
#   - Pasarle los datos a la capa de negocio (Service)
#   - Devolver la respuesta al cliente
#
# Lo que esta capa NO hace:
#   - NO valida reglas de negocio (eso es del Service)
#   - NO guarda ni consulta la base de datos (eso es del Repository)
#   - NUNCA importa el Repository directamente (rompería las capas)

from flask import Flask, request, jsonify
from services.student_service import StudentService  # <- importa SOLO hacia abajo

app = Flask(__name__)
student_service = StudentService()


@app.route("/estudiantes", methods=["POST"])
def registrar_estudiante():
    # 1. Recibir los datos que manda el cliente (el "dto")
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "No se enviaron datos"}), 400

    # 2. Entregar a la capa de negocio. Ella decide si es válido o no.
    try:
        estudiante = student_service.registrar(datos)
    except ValueError as e:
        # Si el Service rechaza el registro (ej: créditos inválidos)
        return jsonify({"error": str(e)}), 400

    # 3. Responder al cliente
    return jsonify({
        "mensaje": "Estudiante registrado con éxito",
        "estudiante": estudiante
    }), 201


if __name__ == "__main__":
    app.run(debug=True, port=5001)