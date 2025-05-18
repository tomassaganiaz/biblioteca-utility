import datetime

class Usuario:
	def __init__(self, nombre: str, id_usuario: int):
		"""Inicializa un usuario con nombre, ID y gestiona datos como multas, historial y feedback."""
		self.nombre = nombre
		self.id_usuario = id_usuario
		self.libros_prestados = {}
		self.historial_prestamos = []
		self.notificaciones = []
		self.reportes = []
		self.recomendaciones = []
		self.multas = 0  # Acumulador de multas
		self.feedback = {}  # Opiniones sobre libros

	def pedir_libro(self, libro):
		"""Solicita un libro si está disponible y no supera el límite de préstamo."""
		if not libro.disponible:
			raise ValueError(f"El libro '{libro.titulo}' no está disponible.")
		if len(self.libros_prestados) >= 3:
			raise ValueError("Has alcanzado el límite de libros prestados (3).")

		libro.disponible = False
		fecha_prestamo = datetime.date.today()
		self.libros_prestados[libro] = fecha_prestamo
		self.historial_prestamos.append((libro, fecha_prestamo))
		self.agregar_notificacion(f"Has pedido prestado '{libro.titulo}'.")
		print(f"Libro '{libro.titulo}' prestado a {self.nombre}.")

	def devolver_libro(self, libro):
		"""Devuelve un libro y calcula multas si se excedió el tiempo de préstamo."""
		if libro not in self.libros_prestados:
			raise ValueError(f"El libro '{libro.titulo}' no está en tu lista de préstamos.")

		fecha_prestamo = self.libros_prestados.pop(libro)
		libro.disponible = True
		dias_prestamo = (datetime.date.today() - fecha_prestamo).days
		if dias_prestamo > 14:  # Plazo máximo permitido
			multa = (dias_prestamo - 14) * 5  # Penalización de 5 por día de retraso
			self.multas += multa
			self.agregar_notificacion(f"Has recibido una multa de {multa} por retraso en '{libro.titulo}'.")

		print(f"Libro '{libro.titulo}' devuelto por {self.nombre}.")

	def calificar_libro(self, libro, calificacion, comentario=""):
		"""Permite a un usuario calificar y opinar sobre un libro."""
		if 1 <= calificacion <= 5:
			self.feedback[libro.titulo] = {"calificacion": calificacion, "comentario": comentario}
			print(f"Calificación registrada: {libro.titulo} - {calificacion} estrellas")
		else:
			raise ValueError("La calificación debe estar entre 1 y 5.")

	def generar_reporte_usuario(self):
		"""Exporta el historial de préstamos y multas en formato CSV."""
		import csv
		nombre_archivo = f"reporte_usuario_{self.id_usuario}.csv"
		with open(nombre_archivo, mode="w", newline="") as archivo:
			escritor = csv.writer(archivo)
			escritor.writerow(["Libro", "Fecha de Préstamo", "Multas Acumuladas"])
			for libro, fecha in self.historial_prestamos:
				escritor.writerow([libro.titulo, fecha, self.multas])
		print(f"Reporte exportado: {nombre_archivo}")

	def agregar_notificacion(self, mensaje):
		"""Añade notificaciones sobre préstamos, devoluciones o penalizaciones."""
		self.notificaciones.append(mensaje)

	def mostrar_notificaciones(self):
		"""Muestra las notificaciones pendientes."""
		if not self.notificaciones:
			print("No tienes notificaciones nuevas.")
		else:
			print("Notificaciones:")
			for notif in self.notificaciones:
				print(f"- {notif}")