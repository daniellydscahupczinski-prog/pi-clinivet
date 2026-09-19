from app.dao.dao import DAO
from app.models.veterinario import Veterinario

class Veterinario_DAO(DAO):
    def __init__(self,database):
        super().__init__(database)

    def save(self, veterinario):
        conexao, cursor = self.conectar()

        try: 
            sql = """INSERT INTO VETERINARIO 
                (NOME, CPF, TELEFONE, RG, ESPECIALIDADE )
                VALUES (%s,%s,%s,%s,%s)"""
            cursor.execute(
                sql,(
                    veterinario.nome, 
                    veterinario.cpf,
                    veterinario.telefone, 
                    veterinario.rg, 
                    veterinario.especialidade
                )
            )
            conexao.commit()
            veterinario.id = cursor.lastrowid
            return veterinario 
        except Exception: 
            conexao.rollback()
            raise
        finally: 
            self.desconectar(cursor, conexao)
    def get_all(self): 
        conexao,cursor = self.conectar()
        try: 
            sql = """ 
                    SELECT ID, NOME, CPF, TELEFONE, RG, ESPECIALIDADE
                    FROM VETERINARIO ORDER BY NOME
"""
            cursor.execute(sql)
            registros = cursor.fetchall()
            veterinario = []
            for registro in registros: 
                veterinario.append(
                    Veterinario(
                        registro[0],
                        registro[1],
                        registro[2],
                        registro[3],
                        registro[4],
                        registro[5]


                    )
                )
            return veterinario 
        finally: 
            self.desconectar(cursor,conexao)

    def get_by_id(self,id):
        conexao, cursor = self.conectar()
        try: 
            sql = """
                    SELECT ID, NOME, CPF, TELEFONE, RG, ESPECIALIDADE 
                    FROM VETERINARIO WHERE ID = %s
"""
            cursor.execute(sql,(id,))
            registro = cursor.fetchone()
            if registro is None: 
                return None
            return Veterinario(
                        registro[0],
                        registro[1],
                        registro[2],
                        registro[3],
                        registro[4],
                        registro[5]               
            )
        finally: 
            self.desconectar(cursor,conexao)
    

    def update(self, veterinario):
        conexao, cursor = self.conectar()
        try: 
            sql = """
                    UPDATE VETERINARIO SET 
                    NOME = %s, 
                    CPF = %s, 
                    TELEFONE = %s,
                    RG = %s, 
                    ESPECIALIDADE = %s 
                    WHERE 
                    ID = %s
"""
            cursor.execute(sql,(
                veterinario.nome,
                veterinario.cpf, 
                veterinario.telefone, 
                veterinario.rg,
                veterinario.especialidade,
                veterinario.id
            ))
            conexao.commit()
            sucesso = cursor.rowcount > 0
            return sucesso 
        except Exception :
            conexao.rollback()
            raise 
        finally: 
            self.desconectar(cursor, conexao)

    def delete(self,id):
        conexao, cursor = self.conectar()
        try: 
            sql = """
                    DELETE FROM VETERINARIO
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