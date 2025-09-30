class Livro:
    """Representa um livro com título, autor e ISBN."""
    def __init__(self, titulo, autor, isbn):
        # O construtor inicializa os atributos do objeto.
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def detalhes(self):
        """Retorna uma string formatada com as informações do livro."""
        #return f"Título: '{self.titulo}' | Autor: {self.autor} | ISBN: {self.isbn}" #podemos usar o return
        print(f"Título: '{self.titulo}' | Autor: {self.autor} | ISBN: {self.isbn}")

# --- PRÁTICA ---
livro1 = Livro("A Arte da Guerra", "Sun Tzu", "978-85-7835-022-7") #objeto livro1
livro2 = Livro("O Alquimista", "Paulo Coelho", "978-85-00-00000-0") #objeto2 livro2

print("--- Livros Criados ---")
print(livro1.detalhes())
print(livro2.detalhes())


#quando lidamos com métodos e funções eles sempre retornam algo e  no lugar de usar prints dentro deles,
# nós usamos o 'return' que no retornará o que colocamos no algoritmo