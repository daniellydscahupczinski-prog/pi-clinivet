from app.dao.dao import DAO
from app.models.animal import Animal

class Animal_DAO(DAO):
    def __init__(self, database):
        super().__init__(database)

    def save(self, animal):
        conexao, cursor = self.conectar()
        try:
            sql = """
                    INSERT INTO ANIMAL
                    (NOME, DATA_NASCIMENTO, SEXO, PESO, CLIENTE_ID, ESPECIE_ID, RACA_ID)
                    VALUES(%s, %s, %s, %s, %s, %s, %s)
                    """
            cursor.execute(sql, (
                animal.nome,
                animal.data_nascimento,
                animal.sexo,
                animal.peso,
                animal.cliente_id,
                animal.especie_id,
                animal.raca_id,
            ))
            conexao.commit()
            animal.id = cursor.lastrowid
            return animal
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
                    ID, NOME, DATA_NASCIMENTO, SEXO, PESO,
                    CLIENTE_ID, ESPECIE_ID, RACA_ID
                FROM
                    ANIMAL
                ORDER BY
                    NOME
                  """
            cursor.execute(sql)
            registros = cursor.fetchall()
            animal = []
            for registro in registros:

                animal.append(
                    Animal(
                        registro[0],
                        registro[1],
                        registro[2],
                        registro[3],
                        registro[4],
                        registro[5],
                        registro[6],
                        registro[7]
                    )
                )
            return animal

        finally:
            self.desconectar(cursor, conexao)

    def get_by_id(self, id):
        conexao, cursor = self.conectar()
        try:
            sql = """
                SELECT 
                    ID, NOME, DATA_NASCIMENTO, SEXO, PESO,
                    CLIENTE_ID, ESPECIE_ID, RACA_ID
                FROM 
                    ANIMAL
                WHERE
                    ID = %s
                  """
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()

            if registro is None:
                return None

            return Animal(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                registro[4],
                registro[5],
                registro[6],
                registro[7]
            )

        finally:
            self.desconectar(cursor, conexao)

    def update(self, animal):
        conexao, cursor = self.conectar()
        try:
            sql = """
                UPDATE ANIMAL SET 
                    NOME = %s,
                    DATA_NASCIMENTO = %s,
                    SEXO = %s,
                    PESO = %s,
                    CLIENTE_ID = %s,
                    ESPECIE_ID = %s,
                    RACA_ID = %s
                WHERE 
                    ID = %s
                  """
            cursor.execute(sql, (
                animal.nome,
                animal.data_nascimento,
                animal.sexo,
                animal.peso,
                animal.cliente_id,
                animal.especie_id,
                animal.raca_id,
                animal.id
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
                        DELETE FROM ANIMAL  
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