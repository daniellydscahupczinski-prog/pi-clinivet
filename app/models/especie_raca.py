class Especie_Raca:
    def __init__(self, especie_id = None, raca_id = None):
        self.especie_id = especie_id
        self.raca_id = raca_id

    @property
    def especie_id(self):
        return self._especie_id
    @especie_id.setter
    def especie_id(self,especie_novo_id):
        self._especie_id = especie_novo_id

    @property 
    def raca_id(self):
        return self._raca_id

    @raca_id.setter
    def raca_id(self, raca_novo_id):
        self._raca_id = raca_novo_id

    def atualizar_dados(self, especie_novo_id,raca_novo_id):
        self._especie_id = especie_novo_id
        self._raca_id = raca_novo_id