from model.libro import Libro

class LibroDigital(Libro):
    def _init_(self, titulo, autor, isbn, tamaño_mb):
        super()._init_(titulo, autor, isbn)
        self.tamaño_mb = tamaño_mb

    def descargar(self):
        return f'📥 Descargando "{self.titulo}"... Tamaño: {self.tamaño_mb} MB.'

    def _str_(self):
        return super()._str_() + f' | Tamaño: {self.tamaño_mb} MB'