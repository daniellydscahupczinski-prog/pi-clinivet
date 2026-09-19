class Veterinario: 
    def __init__(self, id, nome, cpf, telefone, rg, especialidade):
        self.id = id 
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone 
        self.rg = rg
        self.especialidade = especialidade

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    
    @property 
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        self._cpf = novo_cpf

    @property
    def telefone(self):
        return self._telefone
    @telefone.setter
    def telefone(self, novo_telefone):
        self._telefone = novo_telefone

    @property 
    def rg(self):
        return self._rg
    @rg.setter
    def rg(self, novo_rg):
        self._rg = novo_rg

    @property
    def especialidade(self):
        return self._especialidade
    
    @especialidade.setter
    def especialidade(self, nova_especialidade):
        self._especialidade = nova_especialidade

    def atualizar_dados(self,novo_id, novo_nome, novo_cpf, novo_rg, novo_telefone, nova_especialidade):
        self._id = novo_id 
        self._nome = novo_nome
        self._cpf = novo_cpf
        self._rg = novo_rg
        self._telefone = novo_telefone
        self._especialidade = nova_especialidade

    
