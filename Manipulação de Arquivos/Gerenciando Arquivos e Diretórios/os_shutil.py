import os
import shutil
from pathlib import Path

# Armazena o caminho da pasta
ROOT_PATH = Path(__file__).parent

# Cria um novo diretório
# os.mkdir(ROOT_PATH / 'novo-diretorio')

# arquivo = open(ROOT_PATH / "novo.txt", 'w')
# arquivo.close()

# Renomeia um arquivo
# os.rename(ROOT_PATH / 'novo.txt', ROOT_PATH / 'alterado.txt')

# Remove um arquivo
# os.remove(ROOT_PATH / 'alterado.txt')

# Move um arquivo para outro diretório
shutil.move(ROOT_PATH / 'novo.txt', ROOT_PATH / 'novo-diretorio' / 'novo.txt')