from flask import Flask, render_template, request

from model.biblioteca import Biblioteca
from model.usuario import Usuario
from model.libro import Libro

app = Flask(__name__)
biblioteca = Biblioteca()

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/registrar_usuario", methods=["POST"])
def registrar_usuario():
    nombre = request.form["nombre"]
    usuario_id = request.form["usuario_id"]
    usuario = Usuario(nombre, usuario_id)
    mensaje = biblioteca.registrar_usuario(usuario)
    return render_template("index.html", mensaje=mensaje)

@app.route("/agregar_libro", methods=["POST"])
def agregar_libro():
    titulo = request.form["titulo"]
    autor = request.form["autor"]
    isbn = request.form["isbn"]
    libro = Libro(titulo, autor, isbn)
    mensaje = biblioteca.agregar_libro(libro)
    return render_template("index.html", mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)
