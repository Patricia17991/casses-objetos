# --- 1. Classes Entidade ---

class Livro:
    """Representa um livro na biblioteca."""
    def __init__(self, titulo, autor, isbn):
        # Atributos (estado do objeto)
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True  # Status do livro

    def __str__(self):
        # Método especial para representação do objeto (útil para prints)
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"Título: {self.titulo} | Autor: {self.autor} | ISBN: {self.isbn} | Status: {status}"

class Membro:
    """Representa um membro da biblioteca."""
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.livros_emprestados = [] # Lista de objetos Livro

    def __str__(self):
        return f"Membro: {self.nome} | Matrícula: {self.matricula} | Livros Emprestados: {len(self.livros_emprestados)}"

class Emprestimo:
    """Representa a relação de empréstimo entre um Livro e um Membro."""
    def __init__(self, livro, membro):
        # Objetos como atributos: Composição
        self.livro = livro 
        self.membro = membro
        # Uma data simplificada pode ser um atributo, mas vamos focar no essencial por agora

    def __str__(self):
        return f"Empréstimo | Livro: {self.livro.titulo} para Membro: {self.membro.nome}"

# --- 2. Classe Controladora (Lógica de Negócio) ---

class GerenciadorBiblioteca:
    """Gerencia as operações e coleções da biblioteca."""
    def __init__(self):
        # Coleções para armazenar objetos (nosso "banco de dados" temporário)
        self.livros = {}  # Usaremos ISBN como chave para facilitar a busca
        self.membros = {} # Usaremos Matrícula como chave
        self.emprestimos = [] # Lista de objetos Emprestimo

    def adicionar_livro(self, livro):
        """Adiciona um objeto Livro à coleção."""
        if livro.isbn in self.livros:
            print("ERRO: Livro com este ISBN já existe.")
            return
        self.livros[livro.isbn] = livro
        print(f"Livro '{livro.titulo}' adicionado com sucesso.")

    def registrar_membro(self, membro):
        """Adiciona um objeto Membro à coleção."""
        if membro.matricula in self.membros:
            print("ERRO: Membro com esta matrícula já existe.")
            return
        self.membros[membro.matricula] = membro
        print(f"Membro '{membro.nome}' registrado com sucesso.")

    def realizar_emprestimo(self, isbn, matricula):
        """Realiza a lógica de emprestar um livro."""
        livro = self.livros.get(isbn)
        membro = self.membros.get(matricula)

        if not livro:
            print("ERRO: Livro não encontrado.")
            return
        if not membro:
            print("ERRO: Membro não encontrado.")
            return
        
        # Regra de Negócio/Objeto
        if not livro.disponivel:
            print(f"ERRO: O livro '{livro.titulo}' já está emprestado.")
            return

        # 1. Atualiza o estado do Livro
        livro.disponivel = False
        
        # 2. Atualiza a lista de livros do Membro
        membro.livros_emprestados.append(livro)
        
        # 3. Cria e registra o objeto Emprestimo
        novo_emprestimo = Emprestimo(livro, membro)
        self.emprestimos.append(novo_emprestimo)
        
        print(f"SUCESSO: '{livro.titulo}' emprestado para {membro.nome}.")

    def registrar_devolucao(self, isbn):
        """Lógica para registrar a devolução."""
        livro = self.livros.get(isbn)

        if not livro:
            print("ERRO: Livro não encontrado.")
            return

        # Regra de Negócio/Objeto
        if livro.disponivel:
            print(f"AVISO: O livro '{livro.titulo}' já estava disponível.")
            return

        # 1. Atualiza o estado do Livro
        livro.disponivel = True

        # 2. Remove o livro da lista de empréstimos do membro (lógica simplificada)
        # O ideal seria buscar o objeto Emprestimo na lista self.emprestimos para ver quem o pegou.
        for membro in self.membros.values():
            if livro in membro.livros_emprestados:
                membro.livros_emprestados.remove(livro)
                print(f"SUCESSO: '{livro.titulo}' devolvido por {membro.nome}.")
                return
        
        print("ERRO: Não foi possível rastrear quem estava com o livro (possível erro na lógica).")


    def listar_livros(self):
        """Lista todos os livros e seus status."""
        print("\n--- Catálogo de Livros ---")
        for livro in self.livros.values():
            print(livro)

# --- 3. Execução e Teste ---

# 1. Instanciar o Gerenciador (Criação do Objeto principal)
biblioteca = GerenciadorBiblioteca()

# 2. Criar e adicionar Objetos Livro
livro1 = Livro("Padrões de Projeto", "Gang of Four", "978-0201633610")
livro2 = Livro("Código Limpo", "Robert C. Martin", "978-8573934781")
livro3 = Livro("Refatoração", "Martin Fowler", "978-8573932824")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

print("-" * 30)

# 3. Criar e registrar Objetos Membro
membroA = Membro("Alice Silva", "M001")
membroB = Membro("Bruno Santos", "M002")

biblioteca.registrar_membro(membroA)
biblioteca.registrar_membro(membroB)

print("-" * 30)

# 4. Simular Operações (Interação entre Objetos)
print("--- TESTE 1: EMPRÉSTIMO ---")
biblioteca.realizar_emprestimo("978-8573934781", "M001") # Alice pega "Código Limpo"

print("\n--- TESTE 2: TENTATIVA DE EMPRÉSTIMO INDISPONÍVEL ---")
biblioteca.realizar_emprestimo("978-8573934781", "M002") # Bruno tenta pegar o mesmo livro

print("\n--- TESTE 3: NOVO EMPRÉSTIMO ---")
biblioteca.realizar_emprestimo("978-0201633610", "M002") # Bruno pega "Padrões de Projeto"

print("-" * 30)
# 5. Visualizar o estado atual
biblioteca.listar_livros()
print("-" * 30)
print(membroA)
print(membroB)
print("-" * 30)

# 6. Simular Devolução
print("--- TESTE 4: DEVOLUÇÃO ---")
biblioteca.registrar_devolucao("978-8573934781") # Alice devolve "Código Limpo"

print("-" * 30)
biblioteca.listar_livros()