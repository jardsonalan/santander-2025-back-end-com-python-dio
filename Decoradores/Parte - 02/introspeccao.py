from functools import wraps

def meu_decorador(funcao):
  @wraps(funcao) # Serve para evitar erros de introspecção
  def envelope(*args, **kwargs):
    return funcao(*args, **kwargs)

  return envelope

@meu_decorador
def ola_mundo(nome):
  print(f'Olá mundo {nome}!')
  return nome.upper()

print(ola_mundo.__name__)