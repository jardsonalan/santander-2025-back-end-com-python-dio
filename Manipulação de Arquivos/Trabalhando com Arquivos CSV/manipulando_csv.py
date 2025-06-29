import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Escrevendo um arquivo csv
try:
  with open(ROOT_PATH / 'usuarios.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['id', 'nome'])
    escritor.writerow(['1', 'Maria'])
    escritor.writerow(['2', 'João'])
except IOError as exc:
  print(f'Erro ao criar o arquivo: {exc}')

# Lendo um arquivo csv
try:
  with open(ROOT_PATH / 'usuarios.csv', 'r', newline='', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    for row in leitor:
      print(row)
except IOError as exc:
  print(f'Erro ao criar o arquivo: {exc}')

# Exemplo utilizando DictReader
try:
  with open(ROOT_PATH / 'usuarios.csv', newline='') as arquivo:
    leitor = csv.DictReader(arquivo)
    for row in leitor:
      print(f'ID: {row['id']}')
      print(f'Nome: {row['nome']}')
except IOError as exc:
  print(f'Erro ao criar o arquivo: {exc}')