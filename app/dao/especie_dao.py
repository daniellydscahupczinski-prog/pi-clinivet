from app.dao.dao import DAO
from app.models.especie import Especie
from app.models.raca import Raca


class Especie_DAO(DAO):
    def __init__(self, database):
        super().__init__(database)

    def save(self, especie):
        conexao, cursor = self.conectar()
        try:
            sql = """
                INSERT INTO ESPECIE (NOME)
                VALUES (%s)
            """
            cursor.execute(
                sql, (
                    especie.nome,
                )
            )
            conexao.commit()
            especie.id = cursor.lastrowid
            return especie
        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(cursor, conexao)

    def _montar_especie(self, registro):
        # registro: (especie.id, especie.nome, raca.id, raca.nome)
        raca = None
        if registro[2] is not None:
            raca = Raca(registro[2], registro[3])

        return Especie(
            registro[0],
            registro[1],
            raca
        )

    def get_all(self):
        conexao, cursor = self.conectar()
        try:
            sql = """
                SELECT
                    e.ID, e.NOME,
                    r.ID, r.NOME
                FROM ESPECIE e
                LEFT JOIN (
                    SELECT ESPECIE_ID, MIN(RACA_ID) AS RACA_ID
                    FROM ESPECIE_RACA
                    GROUP BY ESPECIE_ID
                ) er ON er.ESPECIE_ID = e.ID
                LEFT JOIN RACA r ON r.ID = er.RACA_ID
                ORDER BY e.NOME
            """
            cursor.execute(sql)
            registros = cursor.fetchall()
            return [self._montar_especie(registro) for registro in registros]

        finally:
            self.desconectar(cursor, conexao)

    def get_by_id(self, id):
        conexao, cursor = self.conectar()
        try:
            sql = """
                SELECT
                    e.ID, e.NOME,
                    r.ID, r.NOME
                FROM ESPECIE e
                LEFT JOIN (
                    SELECT ESPECIE_ID, MIN(RACA_ID) AS RACA_ID
                    FROM ESPECIE_RACA
                    GROUP BY ESPECIE_ID
                ) er ON er.ESPECIE_ID = e.ID
                LEFT JOIN RACA r ON r.ID = er.RACA_ID
                WHERE e.ID = %s
            """
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()

            if registro is None:
                return None

            return self._montar_especie(registro)
        finally:
            self.desconectar(cursor, conexao)

    def update(self, especie):
        conexao, cursor = self.conectar()
        try:
            sql = """
                UPDATE ESPECIE SET
                NOME = %s
                WHERE ID = %s
            """
            cursor.execute(
                sql, (
                    especie.nome,
                    especie.id
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
            # Descobre automaticamente todas as tabelas/colunas que têm
            # chave estrangeira apontando para ESPECIE.ID (ex: ESPECIE_RACA,
            # ANIMAL, etc.) e apaga os vínculos antes de excluir a espécie.
            cursor.execute(
                """
                SELECT TABLE_NAME, COLUMN_NAME
                FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
                WHERE REFERENCED_TABLE_NAME = 'ESPECIE'
                  AND REFERENCED_COLUMN_NAME = 'ID'
                  AND TABLE_SCHEMA = DATABASE()
                """
            )
            dependencias = cursor.fetchall()

            for tabela, coluna in dependencias:
                cursor.execute(
                    f"DELETE FROM {tabela} WHERE {coluna} = %s",
                    (id,)
                )

            sql = """
                DELETE FROM ESPECIE
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