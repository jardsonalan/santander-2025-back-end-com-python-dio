def meu_decorador(funcao):
  def envelope():
    print('Faz algo antes de executar a função.')
    funcao() # Executa a função passado por parâmetro
    print('Faz algo depois de executar a função.')
  
  # Retorna a função envelope sem inicializar
  return envelope

# Utiliza um @ para utilizar decoradores
@meu_decorador
def ola_mundo():
  print('Olá mundo!')

ola_mundo()