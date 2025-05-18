from util.reportes import Reportes
from model.biblioteca import Biblioteca
from model.usuario import Usuario
from model.libro import Libro
from model.biblioteca import Biblioteca

class BibliotecaInteractiva:
    def __init__(self):
        self.biblioteca = Biblioteca()
        self.usuario_actual = None

    def mostrar_menu(self):
        while True:
            print("\n📚 Menú Biblioteca 📚")
            print("1. Registrarse")
            print("2. Agregar un libro")
            print("3. Pedir prestado un libro")
            print("4. Devolver un libro")
            print("5. Buscar libros")
            print("6. Salir")
            
            opcion = input("👉 Selecciona una opción: ")
            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                self.agregar_libro()
            elif opcion == "3":
                self.pedir_prestado()
            elif opcion == "4":
                self.devolver_libro()
            elif opcion == "5":
                self.buscar_libro()
            elif opcion == "6":
                print("👋 ¡Hasta luego!")
                break

    def registrar_usuario(self):
        nombre = input("🆕 Ingresa tu nombre: ")
        usuario_id = input("🔢 Ingresa tu ID: ")
        usuario = Usuario(nombre, usuario_id)
        print(self.biblioteca.registrar_usuario(usuario))
        self.usuario_actual = usuario