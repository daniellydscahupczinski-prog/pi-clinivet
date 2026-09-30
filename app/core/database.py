import mysql.connector
import os
from pathlib import Path
from dotenv import load_dotenv

class Database:

    caminho_env = Path(__file__).resolve().parents[2] / ".env"
    carregou = load_dotenv(caminho_env, override=True, encoding="utf-8-sig")

    def conectar(self):

        print("DEBUG:", self.caminho_env, self.caminho_env.exists(), self.carregou, os.getenv("DB_USER"))

        return mysql.connector.connect(
            host =      os.getenv("DB_HOST"),
            port =      int(os.getenv("DB_PORT", 3306)),
            database =  os.getenv("DB_NAME"),
            user =      os.getenv("DB_USER"),
            password =  os.getenv("DB_PASSWORD")
        )
    def desconectar(self, cursor=None, conexao=None):
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()