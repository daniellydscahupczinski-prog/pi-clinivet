from app.dao.dao import DAO
from app.models.cliente import Cliente

class Cliente_DAO(DAO):
    def __init__(self, database):
        super().__init__(database)

    def save(self, cliente):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    INSERT INTO CLIENTE
                    (
                        NOME,
                        TELEFONE,
                        CPF
                    )
                    VALUES
                    (
                        %s,
                        %s,
                        %s
                    )
                    """
            cursor.execute(
                sql,
                (
                    cliente.nome,
                    cliente.telefone,
                    cliente.cpf
                )
            )

            conexao.commit()

            cliente.id = cursor.lastrowid

            return cliente
        
        except Exception:

            conexao.rollback()
            raise

        finally:

            self.desconectar(cursor, conexao)

    def search(self, termo):
        conexao, cursor = self.conectar()
        try:
            sql = """
                    SELECT
                        ID,
                        NOME,
                        TELEFONE,
                        CPF
                    FROM
                        CLIENTE
                    WHERE
                        NOME LIKE %s
                        OR CPF LIKE %s
                    ORDER BY
                        NOME
                    """
            termo_busca = f"%{termo}%"
            cursor.execute(
                sql,
                (termo_busca, termo_busca)
            )

            registros = cursor.fetchall()
            cliente = []
            for registro in registros:
                cliente.append(
                    Cliente(
                        registro[0],
                        registro[1],
                        registro[2],
                        registro[3]
                    )
                )

            return cliente

        finally:

            self.desconectar(cursor, conexao)

    def get_all(self):
        conexao, cursor = self.conectar()
        try:
            sql = """
                    SELECT
                        ID,
                        NOME,
                        TELEFONE,
                        CPF
                    FROM
                        CLIENTE
                    ORDER BY
                        NOME
                    """
            cursor.execute(sql)
            
            registros = cursor.fetchall()
            cliente = []
            for registro in registros:
                cliente.append(
                    Cliente(
                        registro[0],
                        registro[1],
                        registro[2],
                        registro[3]
                    )
                )

            return cliente
            
        finally:

            self.desconectar(cursor, conexao)

    def get_by_id(self, id):
        conexao, cursor = self.conectar()
        try:
            sql = """
                    SELECT
                        ID,
                        NOME,
                        TELEFONE,
                        CPF
                    FROM
                        CLIENTE
                    WHERE
                        ID = %s
                    """
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()

            if registro is None:
                return None
            
            return Cliente(
                registro[0],
                registro[1],
                registro[2],
                registro[3]
            )

        finally:

            self.desconectar(cursor, conexao)

    def update(self, cliente):
        conexao, cursor = self.conectar()
        try:
            sql = """
                    UPDATE CLIENTE
                    SET
                        NOME = %s,
                        TELEFONE = %s,
                        CPF = %s
                    WHERE
                        ID = %s
                    """
            
            cursor.execute(
                sql,
                (
                    cliente.nome,
                    cliente.telefone,
                    cliente.cpf,
                    cliente.id
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
                    FROM CLIENTE
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