arquivo = open('/home/jardsonalan/Área de trabalho/santander-2025-back-end-com-python/Manipulação de Arquivos/Operação de Escrita/teste.txt', 'w')

# Utilizamos quando estamos trabalhando com uma string grande, já processada
arquivo.write('Escrevendo dados em um novo arquivo.')

# Utilizamos quando queremos interar sobre uma lista
arquivo.writelines(['\n', 'Escrevendo', '\n',  'um', '\n', 'novo', '\n', 'texto'])

arquivo.close()