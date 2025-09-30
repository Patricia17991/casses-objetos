# 1. Função Simples (Autônoma)
# Esta função recebe um número e retorna o resultado da multiplicação por 2.

def dobrar_numero(numero):
  """
  Calcula o dobro de um número.
  """
  resultado = numero * 2
  return resultado  # Usa 'return' para enviar o valor de volta

# ---

# 2. Classe e Método
# Uma classe é um 'molde'. Um método é uma função definida DENTRO de uma classe.

class CalculadoraSimples:
  """
  Uma classe simples para realizar operações básicas.
  """
  def __init__(self, valor_base):
    # O método '__init__' é o construtor; ele define o estado inicial do objeto.
    self.base = valor_base

  def quadruplicar(self):
    """
    Este é um MÉTODO. Ele usa o valor 'self.base' e retorna 4 vezes esse valor.
    """
    quadruplo = self.base * 4
    return quadruplo # Usa 'return' para enviar o valor de volta

# ---

# 3. Execução e Demonstração

# Chamando a FUNÇÃO (dobrar_numero)
valor_inicial = 5
valor_dobrado = dobrar_numero(valor_inicial)
print(f"Função: O dobro de {valor_inicial} é {valor_dobrado}")

# Criando um OBJETO (Instância da classe)
meu_calculo = CalculadoraSimples(valor_base=10) # 'valor_base' é 10

# Chamando o MÉTODO