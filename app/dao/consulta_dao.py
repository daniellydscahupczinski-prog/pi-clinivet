from app.dao.dao import DAO
from app.models.consulta import Consulta

class Consulta_DAO(DAO):
    def __init__(self, database):
        super().__init__(database)
        

    def save(self,consulta):
        conexao, cursor = self.conectar()
        try: 
            if not self.horario_disponivel(
            consulta.data_consulta,
            consulta.horario_consulta
            ):
                return None
            sql = """ 
                        INSERT INTO CONSULTA 
                        (DATA_CONSULTA, HORARIO_CONSULTA, OBSERVACOES)
                        VALUES (%s,%s,%s)
                    """
            cursor.execute(sql,(
                consulta.data_consulta,
                consulta.horario_consulta,
                consulta.observacoes
            ))
            conexao.commit()
            consulta.id = cursor.lastrowid
            return consulta
        except Exception: 
            conexao.rollback()
            raise
        finally:
            self.desconectar(cursor,conexao)

    def get_all(self):
        conexao, cursor = self.conectar()
        try:
            sql = """
                        SELECT ID, DATA_CONSULTA, 
                        HORARIO_CONSULTA, OBSERVACOES, VETERINARIO_ID
                        FROM CONSULTA ORDER BY 
                        DATA_CONSULTA
                    """
            cursor.execute(sql)
            registros = cursor.fetchall()

            consultas = []
            for registro in registros:
                consultas.append(
                    Consulta(
                        registro[0],
                        registro[1],
                        registro[2],
                        registro[3],
                        registro[4]
                    )
                )
            return consultas
        finally:
            self.desconectar(cursor,conexao)

    def get_by_id(self, id):
        conexao, cursor = self.conectar()
        try: 
            sql = """
                    SELECT ID, DATA_CONSULTA,
                    HORARIO_CONSULTA, OBSERVACOES, VETERINARIO_ID
                    FROM CONSULTA
                    WHERE ID = %s
                """
            cursor.execute(sql,(id,))
            registro = cursor.fetchone()
            if registro is None:
                return None
            return Consulta(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                registro[4]
            )
           
        finally: 
            self.desconectar(cursor,conexao)
        

    def update(self,consulta):
        conexao, cursor = self.conectar()
        try:
            sql = """
                        UPDATE CONSULTA SET 
                        DATA_CONSULTA = %s,
                        HORARIO_CONSULTA = %s, 
                        OBSERVACOES = %s
                        WHERE 
                        ID = %s
"""
            cursor.execute(sql,(
                            consulta.data_consulta,
                            consulta.horario_consulta,
                            consulta.observacoes,
                            consulta.id
                ))
            conexao.commit()
            sucesso = cursor.rowcount > 0
            return sucesso
        except Exception:
            conexao.rollback()
            raise 
        finally: 
            self.desconectar(cursor, conexao)

    def delete(self,id):
        conexao, cursor = self.conectar()
        try: 
            sql = """
                    DELETE FROM CONSULTA 
                    WHERE ID = %s

"""
            cursor.execute(sql,(id,))
            conexao.commit()
            sucesso = cursor.rowcount > 0
            return sucesso
        except Exception: 
            conexao.rollback()
            raise
        finally: 
            self.desconectar(cursor, conexao)

    def horario_disponivel(self, data_consulta, horario_consulta):
        conexao, cursor = self.conectar()
        try:
            sql = """
            SELECT ID
            FROM CONSULTA
            WHERE DATA_CONSULTA = %s
            AND HORARIO_CONSULTA = %s
        """

            cursor.execute(sql, (data_consulta, horario_consulta))
            registro = cursor.fetchone()

            return registro is None

        finally:
            self.desconectar(cursor, conexao)