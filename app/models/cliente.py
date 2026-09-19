class Cliente:

    def __init__(
            self,
            id,
            nome,
            telefone,
            cpf
    ):
        self._id = id
        self._nome = nome
        self._telefone = telefone
        self._cpf = cpf

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def nome(self):
        return self._nome.upper()
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, novo_telefone):
        self._telefone = novo_telefone

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        self._cpf = novo_cpf

    def atualizar_dados(
            self,
            novo_nome,
            novo_telefone,
            novo_cpf
    ):
        self._nome = novo_nome
        self._telefone = novo_telefone
        self._cpf = novo_cpf