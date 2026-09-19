from app.models.especie_raca import Especie_Raca
from app.dao.dao import DAO


class Especie_Raca_DAO(DAO):

    def save(self, especie_id, raca_id):

        conexao, cursor = self.conectar()

        try:
            especie_raca = Especie_Raca(
                especie_id,
                raca_id
            )

            sql = """
                INSERT INTO ESPECIE_RACA
                (ESPECIE_ID, RACA_ID)
                VALUES (%s, %s)
            """

            valores = (
                especie_raca.especie_id,
                especie_raca.raca_id
            )

            cursor.execute(sql, valores)
            conexao.commit()

            return especie_raca

        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(cursor, conexao)

    def get_all(self):

        conexao, cursor = self.conectar()

        try:
            sql = """
                SELECT ESPECIE_ID, RACA_ID
                FROM ESPECIE_RACA
                ORDER BY ESPECIE_ID
            """

            cursor.execute(sql)
            registros = cursor.fetchall()

            especie_racas = []

            for registro in registros:
                especie_racas.append(
                    Especie_Raca(
                        registro[0],
                        registro[1]
                    )
                )

            return especie_racas

        finally:
            self.desconectar(cursor, conexao)

    def get_by_id(self, especie_id):

        return self.get_by_especie(especie_id)

    def get_by_especie(self, especie_id):

        conexao, cursor = self.conectar()

        try:
            sql = """
                SELECT ESPECIE_ID, RACA_ID
                FROM ESPECIE_RACA
                WHERE ESPECIE_ID = %s
            """

            cursor.execute(sql, (especie_id,))
            registros = cursor.fetchall()

            especie_racas = []

            for registro in registros:
                especie_racas.append(
                    Especie_Raca(
                        registro[0],
                        registro[1]
                    )
                )

            return especie_racas

        finally:
            self.desconectar(cursor, conexao)

    def update(self, especie_raca):

        conexao, cursor = self.conectar()

        try:
            sql_delete = """
                DELETE FROM ESPECIE_RACA
                WHERE ESPECIE_ID = %s
            """

            cursor.execute(
                sql_delete,
                (especie_raca.especie_id,)
            )

            sql_insert = """
                INSERT INTO ESPECIE_RACA
                (ESPECIE_ID, RACA_ID)
                VALUES (%s, %s)
            """

            cursor.execute(
                sql_insert,
                (
                    especie_raca.especie_id,
                    especie_raca.raca_id
                )
            )

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(cursor, conexao)

    def delete(self, especie_id, raca_id):

        conexao, cursor = self.conectar()

        try:
            sql = """
                DELETE FROM ESPECIE_RACA
                WHERE ESPECIE_ID = %s
                AND RACA_ID = %s
            """

            cursor.execute(
                sql,
                (especie_id, raca_id)
            )

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(cursor, conexao)