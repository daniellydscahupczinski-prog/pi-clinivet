class Especie:
    def __init__(self, id, nome, raca=None):
        self._id = id
        self._nome = nome
        self._raca = raca

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
    def raca(self):
        return self._raca

    @raca.setter
    def raca(self, nova_raca):
        self._raca = nova_raca

    def atualizar_dados(self, novo_id, novo_nome, nova_raca=None):
        self._nome = novo_nome
        self._id = novo_id
        if nova_raca is not None:
            self._raca = nova_raca