from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
  arquivo = open(ROOT_PATH / 'novo-diretorio' / 'novo.txt', 'r')

# NOTE: A exceção é lançada quando o arquivo não é encontrado.
except FileNotFoundError as exc:
  print(f'Arquivo não encontrado: {exc}')

# NOTE: A exceção é lançada quando tentamos abrir um diretório em vez de um arquivo de texto
except IsADirectoryError as exc:
  print(f'Não foi possível abrir o arquivo: {exc}')

# NOTE: A exceção é lançada quando ocorre um erro geral de E/S (entrada/saída)
except IOError as exc:
  print(f'Erro ao abrir o arquivo: {exc}')

# NOTE: A exceção é lançada quando nenhuma das outras exceções forem possíveis de capturar o erro
except Exception as exc:
  print(f'Algum problema ocorreu ao tentar abrir o arquivo: {exc}')