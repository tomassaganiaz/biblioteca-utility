class Biblioteca:
	def __init__(self):
		self.libros = []
		self.usuarios = {}

	def registrar_usuario(self, usuario):
		if usuario.id_usuario in self.usuarios:
			return f'⚠️ {usuario.nombre} ya está registrado.'
		self.usuarios[usuario.id_usuario] = usuario
		return f'✅ {usuario.nombre} ha sido registrado.'

	def agregar_libro(self, libro):
		self.libros.append(libro)
		return f'✅ "{libro.titulo}" ha sido agregado a la biblioteca.'

	def buscar_libro(self, criterio):
		encontrados = [libro for libro in self.libros if criterio.lower() in libro.titulo.lower() or criterio.lower() in libro.autor.lower()]
		return encontrados if encontrados else "⚠️ No se encontraron libros."

	def recomendar_libros(self, usuario):
		autores_prestados = {libro[1] for libro in usuario.historial_prestamos}
		recomendaciones = [libro for libro in self.libros if libro.autor in autores_prestados and libro not in usuario.libros_prestados]
		return f'📢 Recomendaciones para {usuario.nombre}: ' + ", ".join([libro.titulo for libro in recomendaciones])