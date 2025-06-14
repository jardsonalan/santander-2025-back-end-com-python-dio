def calcular(operacao):
  def somar(a, b):
    return a + b
  
  def subtrair(a, b):
    return a - b
  
  match operacao:
    case '+':
      # Não executa a função
      # Apenas retorna
      return somar
    case '-':
      return subtrair

operacao = calcular('+')
print(operacao(2, 2))