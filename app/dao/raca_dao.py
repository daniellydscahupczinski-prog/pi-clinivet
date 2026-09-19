from app.dao.dao import DAO
from app.models.raca import Raca


class Raca_DAO(DAO):
    def __init__(self, database):
        super().__init__(database)

    def save(self, raca):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    INSERT INTO RACA
                    (
                        NOME
                    )
                    VALUES
                    (
                        %s
                    )
                  """

            cursor.execute(
                sql,
                (
                    raca.nome,
                )
            )

            conexao.commit()

            raca.id = cursor.lastrowid

            return raca

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
                        ID,
                        NOME
                    FROM
                        RACA
                    ORDER BY
                        NOME
                  """

            cursor.execute(sql)

            registros = cursor.fetchall()

            raca = []

            for registro in registros:
                raca.append(
                    Raca(
                        registro[0],
                        registro[1]
                    )
                )

            return raca

        finally:

            self.desconectar(cursor, conexao)

    def get_by_id(self, id):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    SELECT
                        ID,
                        NOME
                    FROM
                        RACA
                    WHERE
                        ID = %s
                  """

            cursor.execute(sql, (id,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            return Raca(
                registro[0],
                registro[1]
            )

        finally:

            self.desconectar(cursor, conexao)

    def update(self, raca):
        conexao, cursor = self.conectar()

        try:

            sql = """
                    UPDATE RACA
                    SET
                        NOME = %s
                    WHERE
                        ID = %s
                    """
            
            cursor.execute(
                sql,
                (
                    raca.nome,
                    raca.id
                )
            )

            conexao.commit()

            return cursor.rowcount > 0
        
        except Exception:

            conexao.rollback()
            raise

        finally:

            self.desconectar(cursor, conexao)

    def delete(self, id):
        conexao, cursor = self.conectar()

        try:

            sql = """
                    DELETE
                    FROM raca
                    WHERE ID = %s
                  """

            cursor.execute(sql, (id,))

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:

            conexao.rollback()
            raise

        finally:

            self.desconectar(cursor, conexao)