import os
from dotenv import dotenv_values
from loguru import logger
import sys
from InquirerPy import inquirer

def load_environment(env: str) -> dict:
    """
    Carrega variáveis de um arquivo .env específico, baseado no ambiente fornecido.

    Args:
        env (str): Nome do ambiente ('development', 'qa', 'homolog', 'production').

    Returns:
        dict: Um dicionário contendo as variáveis carregadas do arquivo .env.
    """
    env = env.strip().lower()
    valid_environments = ["development", "qa", "homolog", "production"]

    if env not in valid_environments:
        raise ValueError(f"Ambiente inválido: {env}. Escolha entre: {', '.join(valid_environments)}")

    dotenv_path = os.path.join("config", "environments", f"{env}.env")
    if not os.path.exists(dotenv_path):
        raise FileNotFoundError(f"Arquivo de configuração {dotenv_path} não encontrado.")

    # Carregar as variáveis diretamente do arquivo .env (sem usar os.environ)
    return dotenv_values(dotenv_path)


# Solicitar ao usuário o ambiente, se necessário
def get_environment_from_user():
    env = input("Selecione o ambiente (development, qa, homolog, production): ").strip().lower()
    return env

def select_environment():
    choices = ['development', 'qa', 'homolog', 'production']
    answer = inquirer.select(
        message="Selecione uma opção:",
        choices=choices,
    ).execute()
    return answer

# Carregar o ambiente definido ou pedir ao usuário
try:
    selected_env = select_environment()
    config = load_environment(selected_env)
except Exception as e:
    print(f"Erro ao carregar o ambiente: {e}")
    sys.exit(1)

# Configurações do projeto
API_BASE_URL = config.get("API_BASE_URL")
AUTH_TOKEN = config.get("AUTH_TOKEN")
LOG_LEVEL = config.get("LOG_LEVEL", "INFO")
LOG_FILE_PATH = config.get("LOG_FILE_PATH", f"logs/{selected_env}_project.log")

# Configuração do Loguru para log no console e em arquivo
logger.remove()  # Remove qualquer configuração padrão

# Log no console
logger.add(
    sys.stdout,
    level=LOG_LEVEL,
    format="{time} - {level} - {message}"
)

# Log em arquivo
logger.add(
    LOG_FILE_PATH,
    level=LOG_LEVEL,
    format="{time} - {level} - {message}",
    rotation="10 MB",  # Faz rotação do log quando atingir 10 MB
    compression="zip"  # Comprime arquivos antigos
)

# Logs iniciais
logger.info(f"Ambiente carregado: {selected_env}")
logger.info(f"API Base URL: {API_BASE_URL}")
