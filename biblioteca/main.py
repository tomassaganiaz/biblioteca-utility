from flask import Flask, render_template, request
from model.libro import Libro
from model.biblioteca import Biblioteca
from model.usuario import Usuario
import datetime

biblioteca = Biblioteca()
app = Flask(__name__)

@app.route("/")
def index():
	return render_template(template_name_or_list="index.html")

@app.route("/registrar_usuario", methods=["POST"])
def registrar_usuario():
	nombre = request.form["nombre"]
	usuario_id = request.form["usuario_id"]
	usuario = Usuario(nombre, usuario_id)
	mensaje = biblioteca.registrar_usuario(usuario)
	return mensaje, 201

@app.route("/agregar_libro", methods=["POST"])
def agregar_libro():
	titulo = request.form["titulo"]
	autor = request.form["autor"]
	isbn = request.form["isbn"]
	libro = Libro(titulo, autor, isbn)
	mensaje = biblioteca.agregar_libro(libro)
	return mensaje, 201

def main():
	"""Función principal para la gestión avanzada de la biblioteca."""

	global biblioteca

	# Agregar libros de prueba
	libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "123456")
	libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "789012")
	libro3 = Libro("1984", "George Orwell", "345678")  # No disponible inicialmente

	biblioteca.agregar_libro(libro1)
	biblioteca.agregar_libro(libro2)
	biblioteca.agregar_libro(libro3)

	# Registrar usuarios
	usuario1 = Usuario("Tomas", 101)
	usuario2 = Usuario("Ana", 102)

	biblioteca.registrar_usuario(usuario1)
	biblioteca.registrar_usuario(usuario2)

	# Simular operaciones avanzadas
	try:
		usuario1.pedir_libro(libro1)
		usuario1.pedir_libro(libro2)

		usuario1.devolver_libro(libro1)

		#usuario1.reservar_libro(libro3)  # Libro no disponible, se reserva

		usuario1.calificar_libro(libro2, 5, "Una obra maestra de la literatura.")

		usuario1.generar_reporte_usuario()

		usuario1.mostrar_notificaciones()

		# Simulación de multa al devolver tarde
		fecha_prestamo = datetime.date.today() - datetime.timedelta(days=20)
		usuario1.libros_prestados[libro3] = fecha_prestamo  # Simula préstamo retrasado
		usuario1.devolver_libro(libro3)

		usuario1.mostrar_notificaciones()

	except ValueError as e:
		print(f"Error: {e}")
		
if __name__ == "__main__":
	main()
	app.run(debug=True)