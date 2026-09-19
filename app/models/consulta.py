class Consulta:
    def __init__(self, id, data_consulta, horario_consulta, observacoes, veterinario_id=None):
        self._id = id
        self._data_consulta = data_consulta
        self._horario_consulta = horario_consulta
        self._observacoes = observacoes
        self._veterinario_id = veterinario_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property 
    def horario_consulta(self):
        return self._horario_consulta
    
    @horario_consulta.setter
    def horario_consulta(self,novo_horario_consulta):
        self._horario_consulta = novo_horario_consulta

    @property 
    def data_consulta(self):
        return self._data_consulta
    @data_consulta.setter
    def data_consulta(self,nova_data_consulta):
        self._data_consulta = nova_data_consulta

    @property
    def observacoes(self):
        return self._observacoes
    
    @observacoes.setter
    def observacoes(self,nova_observacao):
        self._observacoes = nova_observacao

    @property
    def veterinario_id(self):
        return self._veterinario_id

    @veterinario_id.setter
    def veterinario_id(self, novo_veterinario_id):
        self._veterinario_id = novo_veterinario_id

    def atualizar_dados(self,novo_horario_consulta,nova_data_consulta,novas_observacoes):
        horarios_disponiveis = {
            "08:00",
            "09:30",
            "11:00",
            "12:30",
            "14:00",
            "15:30",
            "17:00",
            
        }
        datas_disponíveis = {
            "19/10",
            "20/10",
            "22/10",
            "23/10",
            "25/10",
            "26/10",
            "27/10",
            "28/10"
        }
        if novo_horario_consulta not in horarios_disponiveis:
            return False
        if nova_data_consulta not in datas_disponíveis:
            return False
        self._horario_consulta = novo_horario_consulta
        self._data_consulta = nova_data_consulta
        self._observacoes = novas_observacoes

        return True