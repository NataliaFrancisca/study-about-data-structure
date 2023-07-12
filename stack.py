# último a entrar é o primeiro a sair
class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

class PilhaDeLivros:
    def __init__(self):
        self.pilhaLivros = []
    
    def push(self, nome, autor, paginas):
        livro = Livro(nome, autor, paginas)
        self.pilhaLivros.append(livro)

    def pop(self):
        if(len(self.pilhaLivros) < 1):
            print('Nenhum livro na pilha')
        self.pilhaLivros.pop();
        
    def print(self):
        for x in self.pilhaLivros:
            print(x.titulo)

    def ultimoLivro(self):
        livro = self.pilhaLivros[-1];
        print(livro.titulo)


pilhaLivros = PilhaDeLivros()
pilhaLivros.push('Pachinko', 'Min Jee Lee', 430)
pilhaLivros.push('All About Love', 'Bell Hooks', 220)
pilhaLivros.pop();
# pilhaLivros.print();
pilhaLivros.ultimoLivro();