class Aplicacao_Vacina:

    def __init__(self, id, tipo_servico, data_vacina, horario_vacina, status_vacina, animal_id, vacina_id):
        self._id = id
        self._tipo_servico = tipo_servico
        self._data_vacina = data_vacina
        self._horario_vacina = horario_vacina
        self._status_vacina = status_vacina
        self._animal_id = animal_id
        self._vacina_id = vacina_id

    @property 
    def id(self):
        return self._id
    @id.setter 
    def id(self, novo_id):
        self._id = novo_id

    @property
    def tipo_servico(self):
        return self._tipo_servico
    @tipo_servico.setter
    def tipo_servico(self, novo_tipo_servico):
        self._tipo_servico = novo_tipo_servico

    @property
    def data_vacina(self):
        return self._data_vacina
    @data_vacina.setter
    def data_vacina(self, nova_data_vacina):
        self._data_vacina = nova_data_vacina

    @property
    def horario_vacina(self):
        return self._horario_vacina
    @horario_vacina.setter
    def horario_vacina(self, novo_horario_vacina):
        self._horario_vacina = novo_horario_vacina

    @property
    def status_vacina(self):
        return self._status_vacina
    @status_vacina.setter
    def status_vacina(self, novo_status_vacina):
        self._status_vacina = novo_status_vacina

    @property
    def animal_id(self):
        return self._animal_id
    @animal_id.setter
    def animal_id(self, novo_animal_id):
        self._animal_id = novo_animal_id

    @property
    def vacina_id(self):
        return self._vacina_id
    @vacina_id.setter
    def vacina_id(self, novo_vacina_id):
        self._vacina_id = novo_vacina_id


    def atualizar_dados(self, novo_tipo_servico, nova_data_vacina, novo_horario_vacina, novo_status_vacina, novo_animal_id, novo_vacina_id):
        self._tipo_servico = novo_tipo_servico
        self._data_vacina = nova_data_vacina
        self._horario_vacina = novo_horario_vacina
        self._status_vacina = novo_status_vacina
        self._animal_id = novo_animal_id
        self._vacina_id = novo_vacina_id
