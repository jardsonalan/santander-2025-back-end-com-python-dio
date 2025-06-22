arquivo = open('/home/jardsonalan/Área de trabalho/santander-2025-back-end-com-python/Manipulação de Arquivos/Operação de Leitura/lorem.txt', 'r')

# Ler todo o conteúdo do arquivo de uma vez
# print(arquivo.read())

# Lê uma linha por vez
# print(arquivo.readline())

# Retorna uma lista onde cada elemento é uma linha do arquivo
# print(arquivo.readlines())

# Serve para explorar um arquivo grande utilizando um script rápido
# := - Serve para atribuir um valor a variável
while len(linha := arquivo.readline()):
  print(linha)

arquivo.close()