from app.dao.dao import DAO
from app.models.vacina import Vacina

class Vacina_DAO(DAO):
    def __init__(self, database):
        super().__init__(database)

    def save(self, vacina):
        conexao, cursor = self.conectar()
        try:
            sql = """
                    INSERT INTO VACINA
                    (NOME, DESCRICAO)
                    VALUES(%s, %s)
                    """
            cursor.execute(sql, (
                vacina.nome,
                vacina.descricao,
            ))
            conexao.commit()
            vacina.id = cursor.lastrowid
            return vacina
        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(cursor, conexao)

    def get_all(self):
        conexao, cursor = self.conectar()
        try:
            sql = """
                SELECT
                    ID, NOME, DESCRICAO
                FROM
                    VACINA
                ORDER BY
                    NOME
                  """
            cursor.execute(sql)
            registros = cursor.fetchall()
            vacinas = []
            for registro in registros:
                vacinas.append(
                    Vacina(
                        registro[0],
                        registro[1],
                        registro[2]
                    )
                )
            return vacinas
        finally:
            self.desconectar(cursor, conexao)

    def get_by_id(self, id):
        conexao, cursor = self.conectar()
        try:
            sql = """
                SELECT 
                    ID, NOME, DESCRICAO
                FROM 
                    VACINA
                WHERE
                    ID = %s
                  """
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()
            if registro is None:
                return None
            return Vacina(
                registro[0],
                registro[1],
                registro[2]
            )
        finally:
            self.desconectar(cursor, conexao)

    def update(self, vacina):
        conexao, cursor = self.conectar()
        try:
            sql = """
                UPDATE VACINA SET 
                    NOME = %s,
                    DESCRICAO = %s
                WHERE 
                    ID = %s
                  """
            cursor.execute(sql, (
                vacina.nome,
                vacina.descricao,
                vacina.id
            ))
            conexao.commit()
            sucesso = cursor.rowcount > 0
            return sucesso
        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(cursor, conexao)

    def delete(self, id):
        conexao, cursor = self.conectar()
        try:
            sql = """
                        DELETE FROM VACINA  
                        WHERE ID = %s
                    """
            cursor.execute(sql, (id,))
            conexao.commit()
            sucesso = cursor.rowcount > 0
            return sucesso
        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(cursor, conexao)