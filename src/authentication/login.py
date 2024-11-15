from loguru import logger
from utils.http import make_request
from config.settings import API_BASE_URL

def login():
    try:
        logger.info("Iniciando processo de autenticação.")
        endpoint = f"{API_BASE_URL}/auth/login"
        response = make_request("POST", endpoint, json={"username": "user", "password": "pass"})
        logger.success(f"Login bem-sucedido! Token: {response.json().get('token')}")
        return response.json()
    except Exception as e:
        logger.error(f"Erro durante o login: {e}")
        raise

if __name__ == "__main__":
    login()
