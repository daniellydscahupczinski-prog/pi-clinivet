from app.models.agendamento import Agendamento

class Agendamento_Controller:
    def __init__(
        self,
        dao,
        view
    ):
        self.dao = dao
        self.view = view
        self.agendamento_selecionado = None

    def new(self):
        self.view.limpar_campos()

    def save(self):
        try:
            servico_agendamento, horario_agendamento, data_agendamento, status_agendamento, animal_id = self.view.ler_dados_agendamento()
            agendamento = Agendamento(
                None,
                servico_agendamento,
                data_agendamento,
                horario_agendamento,
                status_agendamento,
                animal_id
            )
            self.dao.save(agendamento)
            self.get_all()
            self.view.exibir_mensagem((("Agendamento cadastrado")))
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def get_all(self):
        agendamento = self.dao.get_all()
        self.view.exibir_agendamento(agendamento)
    
    def selecionar_agendamento(self, event):
        try:
            id_agendamento = self.view.get_id_selecionado()
            self.agendamento_selecionado = self.dao.get_by_id(
                id_agendamento
            )
        except IndexError:
            pass

    def update(self):
        try:
            if self.agendamento_selecionado is None:
                self.view.exibir_mensagem((("Selecione um agendamento da lista", False)))
                return
            servico_agendamento, horario_agendamento, data_agendamento, status_agendamento, animal_id = self.view.ler_dados_agendamento()
            self.agendamento_selecionado.atualizar_dados(
                servico_agendamento,
                data_agendamento,
                horario_agendamento,
                status_agendamento,
                animal_id
            )
            self.dao.update(self.agendamento_selecionado)
            self.get_all()
            self.view.exibir_mensagem((("Agendamento atualizado")))
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def delete(self):
        if self.agendamento_selecionado is None:
            self.view.exibir_mensagem((("Selecione um agendamento da lista", False)))
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.agendamento_selecionado.id)
            if sucesso:
                self.agendamento_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem((("Agendamento excluido")))
            else:
                self.view.exibir_mensagem((("Agendamento nao encontrado", False)))
        except Exception as e:
            self.view.exibir_mensagem((("Problomas ao excluir agendamento", False)))