import os
from dotenv import load_dotenv
from loguru import logger
import sys

# Função para carregar o arquivo .env correto com base no ambiente
def load_environment():
    env = os.getenv("ENV")  # Checa variável de ambiente do sistema
    if not env:  # Caso não tenha sido definida, solicita ao usuário
        env = input("Selecione o ambiente (development, qa, homolog, prod): ").strip().lower()
        os.environ["ENV"] = env  # Define como variável de ambiente global

    dotenv_path = os.path.join("config", "environments", f"{env}.env")
    if not os.path.exists(dotenv_path):
        raise FileNotFoundError(f"Arquivo de configuração {dotenv_path} não encontrado.")
    
    load_dotenv(dotenv_path)
    return env

# Carregar as variáveis do ambiente
ENV = load_environment()

# Configurações do projeto
API_BASE_URL = os.getenv("API_BASE_URL")  # URL base da API
AUTH_TOKEN = os.getenv("AUTH_TOKEN")  # Token de autenticação
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")  # Nível de log padrão

# Configuração do Loguru para log no console e em arquivo
LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", f"logs/{ENV}_project.log")
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
logger.info(f"Ambiente carregado: {ENV}")
logger.info(f"API Base URL: {API_BASE_URL}")
