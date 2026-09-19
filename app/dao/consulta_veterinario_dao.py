from app.dao.dao import DAO
from app.models.consulta_veterinario import Consulta_Veterinario


class Consulta_Veterinario_DAO(DAO):
    def __init__(self, database):
        super().__init__(database)

    def save(self, consulta_veterinario):
        """
        Não existe uma tabela CONSULTA_VETERINARIO separada no banco atual.
        A relação é guardada direto na coluna veterinario_id da tabela consulta.
        Por isso 'save' aqui atualiza o veterinário responsável por uma consulta
        já existente (equivalente a um update).
        """
        conexao, cursor = self.conectar()
        try:
            sql = """
                UPDATE consulta
                SET veterinario_id = %s
                WHERE id = %s
            """
            cursor.execute(sql, (
                consulta_veterinario.veterinario_id,
                consulta_veterinario.consulta_id
            ))
            conexao.commit()
        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(cursor, conexao)

    def get_all(self):
        conexao, cursor = self.conectar()
        try:
            sql = """
                SELECT id, veterinario_id
                FROM consulta
                WHERE veterinario_id IS NOT NULL
            """
            cursor.execute(sql)
            registros = cursor.fetchall()
            resultado = []
            for registro in registros:
                resultado.append(
                    Consulta_Veterinario(
                        consulta_id=registro[0],
                        veterinario_id=registro[1]
                    )
                )
            return resultado
        finally:
            self.desconectar(cursor, conexao)

    def get_by_id(self, id):
        conexao, cursor = self.conectar()
        try:
            sql = """
                SELECT id, veterinario_id
                FROM consulta
                WHERE id = %s
            """
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()
            if registro is None:
                return None
            return Consulta_Veterinario(
                consulta_id=registro[0],
                veterinario_id=registro[1]
            )
        finally:
            self.desconectar(cursor, conexao)

    def update(self, consulta_veterinario):
        conexao, cursor = self.conectar()
        try:
            sql = """
                UPDATE consulta
                SET veterinario_id = %s
                WHERE id = %s
            """
            cursor.execute(sql, (
                consulta_veterinario.veterinario_id,
                consulta_veterinario.consulta_id
            ))
            conexao.commit()
        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(cursor, conexao)

    def delete(self, id):
        """
        'Deletar' a relação aqui significa remover o veterinário
        associado à consulta (não apaga a consulta em si).
        """
        conexao, cursor = self.conectar()
        try:
            sql = """
                UPDATE consulta
                SET veterinario_id = NULL
                WHERE id = %s
            """
            cursor.execute(sql, (id,))
            conexao.commit()
        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(cursor, conexao)