# Serve para duplicar os valores de uma lista
class MeuIterador:
  def __init__(self, numeros: list[int]):
    self.numeros = numeros
    self.contador = 0

  # Serve para retorna valores
  def __iter__(self):
    return self # Retorna o próprio objeto

  def __next__(self):
    try:
      numero = self.numeros[self.contador]
      self.contador += 1
      return numero * 2
    except IndexError:
      raise StopIteration # Condição de parada

for i in MeuIterador(numeros=[38, 13, 11]):
  print(i)