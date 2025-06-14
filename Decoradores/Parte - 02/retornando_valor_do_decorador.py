def meu_decorador(funcao):
  def envelope(*args, **kwargs):
    return funcao(*args, **kwargs)

  return envelope

@meu_decorador
def ola_mundo(nome):
  print(f'Olá mundo {nome}!')
  return nome.upper()

resultado = ola_mundo('Jardson')
print(resultado)