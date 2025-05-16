class Biclioteca:
    def __init__(self):
        self.__livros = []
        self.__usuarios = []
        self.__emprestimos = []

    def adicionar_livro(self, livro):
        self.__livros.append(livro)

    def adicionar_usuario(self, usuario):
        self.__usuarios.append(usuario)

    def emprestar_livro(self, livro, usuario):
        if livro in self.__livros and usuario in self.__usuarios:
            self.__emprestimos.append((livro, usuario))
            return True
        return False

    def devolver_livro(self, livro, usuario):
        if (livro, usuario) in self.__emprestimos:
            self.__emprestimos.remove((livro, usuario))
            return True
        return False