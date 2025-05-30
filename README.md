# Trabajo Práctico POO

Trabajo Práctico n-2: Desarrollo de sistemas Orientado a Objetos

Gestión de Biblioteca
Objetivo:
Modelar un sistema simple para gestionar una biblioteca
 aplicando conceptos de Programación Orientada a Objetos (POO):
   - clases,
   - objetos,
   - atributos,
   - métodos (funciones),
   - herencia
   - y encapsulamiento.

Requisitos:
 - Crear las siguientes clases:

   - Libro: título, autor, ISBN, disponible (bool)

   - Usuario: nombre, ID, libros prestados (máximo 3)

   - Biblioteca: lista de libros y usuarios registrados

Funcionalidades (Métodos):

Un Usuario puede:

 - Pedir prestado un libro (si está disponible y no superó el límite)

 - Devolver un libro

La Biblioteca puede:

 - Registrar usuarios

 - Agregar libros

 - Buscar libros por título o autor

Extra (opcional):

Crear una clase LibroDigital que herede de Libro, pero agregue un atributo de tamaño (MB) y un método para “descargar”.

Manejar errores como: “libro no disponible”, “usuario no registrado”, etc.

Nota: Entregable debe estar versionado
