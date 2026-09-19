class Agendamento:

    def __init__(
            self,
            id,
            servico,
            data_agendamento,
            horario_agendamento,
            status_agendamento,
            animal_id=None
    ):
        self._id = id
        self._servico = servico
        self._data_agendamento = data_agendamento
        self._horario_agendamento = horario_agendamento
        self._status_agendamento = status_agendamento
        self._animal_id = animal_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def servico(self):
        return self._servico

    @servico.setter
    def servico(self, novo_servico):
        self._servico = novo_servico

    @property
    def data_agendamento(self):
        return self._data_agendamento

    @data_agendamento.setter
    def data_agendamento(self, nova_data_agendamento):
        self._data_agendamento = nova_data_agendamento

    @property
    def horario_agendamento(self):
        return self._horario_agendamento

    @horario_agendamento.setter
    def horario_agendamento(self, novo_horario_agendamento):
        self._horario_agendamento = novo_horario_agendamento

    @property
    def status_agendamento(self):
        return self._status_agendamento

    @status_agendamento.setter
    def status_agendamento(self, novo_status_agendamento):
        self._status_agendamento = novo_status_agendamento

    @property
    def animal_id(self):
        return self._animal_id

    @animal_id.setter
    def animal_id(self, novo_animal_id):
        self._animal_id = novo_animal_id

    def atualizar_dados(
            self,
            novo_servico,
            nova_data_agendamento,
            novo_horario_agendamento,
            novo_status_agendamento,
            novo_animal_id=None
    ):
        self._servico = novo_servico
        self._data_agendamento = nova_data_agendamento
        self._horario_agendamento = novo_horario_agendamento
        self._status_agendamento = novo_status_agendamento
        self._animal_id = novo_animal_id