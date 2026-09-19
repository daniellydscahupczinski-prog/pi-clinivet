class Animal: 

    def __init__(self, id, nome, data_nascimento, sexo, peso, cliente_id, especie_id, raca_id):
        self._id = id
        self._nome = nome
        self._data_nascimento = data_nascimento
        self.sexo = sexo 
        self.peso = peso
        self.cliente_id = cliente_id 
        self.especie_id = especie_id 
        self.raca_id = raca_id 

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
    def data_nascimento(self):
        return self._data_nascimento
    @data_nascimento.setter
    def data_nascimento(self, nova_data_nascimento):
        self._data_nascimento = nova_data_nascimento
    
    @property
    def sexo(self):
        return self._sexo
    @sexo.setter 
    def sexo(self, novo_sexo):
        self._sexo = novo_sexo 

    @property 
    def peso(self):
        return self._peso 
    @peso.setter
    def peso(self, novo_peso):
        self._peso = novo_peso

    @property
    def cliente_id(self):
        return self._cliente_id
    @cliente_id.setter 
    def cliente_id(self, novo_cliente_id):
        self._cliente_id = novo_cliente_id

    @property
    def especie_id(self):
        return self._especie_id
    @especie_id.setter
    def especie_id(self, nova_especie_id):
        self._especie_id = nova_especie_id

    @property
    def raca_id(self):
        return self._raca_id
    @raca_id.setter 
    def raca_id(self, nova_raca_id):
        self._raca_id = nova_raca_id

    def atualizar_dados(self, novo_nome, nova_data_nascimento, novo_sexo, novo_peso, novo_cliente_id, nova_especie_id, nova_raca_id):
        self._nome = novo_nome
        self._data_nascimento = nova_data_nascimento
        self._peso = novo_peso
        self._sexo = novo_sexo
        self._cliente_id = novo_cliente_id
        self._especie_id = nova_especie_id
        self._raca_id = nova_raca_id