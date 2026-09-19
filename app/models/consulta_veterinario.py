class Consulta_Veterinario:

    def __init__(self, consulta_id=None, veterinario_id=None):
        self.consulta_id = consulta_id
        self.veterinario_id = veterinario_id

    @property
    def consulta_id(self):
        return self._consulta_id

    @consulta_id.setter
    def consulta_id(self, consulta_novo_id):
        self._consulta_id = consulta_novo_id

    @property
    def veterinario_id(self):
        return self._veterinario_id

    @veterinario_id.setter
    def veterinario_id(self, novo_veterinario_id):
        self._veterinario_id = novo_veterinario_id

    def atualizar_dados(self, novo_veterinario_id, consulta_novo_id):
        self._consulta_id = consulta_novo_id
        self._veterinario_id = novo_veterinario_id