import qrcode

class Libro:
	def __init__(self, titulo, autor, isbn):
		self.titulo = titulo
		self.autor = autor
		self.isbn = isbn
		self.disponible = True
		self.estado = "Bueno"
		self.reservas = []
		self.reseñas = []

	def prestar(self, usuario):
		if not self.disponible:
			return f'⚠️ El libro "{self.titulo}" no está disponible.'
		if self.estado == "Dañado":
			return f'⚠️ "{self.titulo}" está dañado y no puede prestarse.'
		
		self.disponible = False
		usuario.registrar_historial(self, "Préstamo")
		usuario.registrar_prestamo_activo(self)
		return f'✅ "{self.titulo}" ha sido prestado a {usuario.nombre}.'

	def devolver(self, usuario):
		if self.disponible:
			return f'⚠️ Error: "{self.titulo}" ya estaba disponible.'
		
		self.disponible = True
		usuario.registrar_historial(self, "Devolución")
		usuario.eliminar_prestamo_activo(self)
		return f'✅ "{self.titulo}" ha sido devuelto por {usuario.nombre}.'

	def reportar_daño(self, usuario, descripcion):
		self.estado = "Dañado"
		usuario.registrar_daño(self, descripcion)
		return f'⚠️ "{self.titulo}" ha sido reportado como dañado.'

	def generar_qr(self):
		datos = f'Título: {self.titulo}\nAutor: {self.autor}\nISBN: {self.isbn}\nEstado: {self.estado}'
		qr = qrcode.make(datos)
		qr.save(f'{self.titulo.replace(" ", "_")}.png')
		return f'✅ QR generado para "{self.titulo}".'

	def agregar_reseña(self, usuario, calificacion, comentario):
		if calificacion < 1 or calificacion > 5:
			return f'⚠️ Calificación inválida. Debe ser entre 1 y 5.'
		
		self.reseñas.append({
			"usuario": usuario.nombre,
			"calificacion": calificacion,
			"comentario": comentario
		})
		return f'✅ {usuario.nombre} ha calificado "{self.titulo}" con {calificacion} estrellas.'

	def ver_reseñas(self):
		if not self.reseñas:
			return f'📭 No hay reseñas para "{self.titulo}".'
		
		lista_reseñas = "\n".join(
			[f'{r["usuario"]} - ⭐ {r["calificacion"]}: {r["comentario"]}' for r in self.reseñas]
		)
		return f'📝 Reseñas de "{self.titulo}":\n{lista_reseñas}'