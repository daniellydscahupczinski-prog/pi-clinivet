from app.models.consulta import Consulta
from app.models.consulta_veterinario import Consulta_Veterinario


class Consulta_Controller:
    def __init__(
        self,
        consulta_veterinario_dao,
        consulta_dao,
        veterinario_dao,
        view
    ):
        self.consulta_veterinario_dao = consulta_veterinario_dao
        self.consulta_dao = consulta_dao
        self.veterinario_dao = veterinario_dao
        self.view = view
        self.consulta_selecionada = None

    def new(self):
        self.view.limpar_campos()
        self.consulta_selecionada = None

    def carregar_veterinarios(self):
        veterinarios = self.veterinario_dao.get_all()
        self.view.carregar_veterinarios(veterinarios)

    def save(self):
        try:
            data_consulta, horario_consulta, observacoes = \
                self.view.ler_dados_consulta()

            veterinario = self.view.get_veterinario_selecionado()

            if veterinario is None:
                self.view.exibir_mensagem(
                    "Selecione um veterinário!"
                )
                return

            consulta = Consulta(
                None,
                data_consulta,
                horario_consulta,
                observacoes
            )

            self.consulta_dao.save(consulta)

            consulta_veterinario = Consulta_Veterinario(
                consulta.id,
                veterinario.id
            )
            self.consulta_veterinario_dao.save(consulta_veterinario)

            self.get_all()

            self.view.exibir_mensagem(
                "Consulta agendada com sucesso!"
            )

        except ValueError:
            self.view.exibir_mensagem(
                "Erro ao cadastrar consulta!"
            )

    def get_all(self):
        consultas = self.consulta_dao.get_all()

        for consulta in consultas:
            veterinario = self.veterinario_dao.get_by_id(
                consulta.veterinario_id
            )
            consulta.veterinario = veterinario.nome if veterinario else ""

        self.view.exibir_consulta(consultas)

    def selecionar_consulta(self, event):
        try:
            id_consulta = self.view.get_id_selecionado()
            self.consulta_selecionada = self.consulta_dao.get_by_id(
                id_consulta
            )
            self.view.preencher_campos(
                self.consulta_selecionada
            )
        except IndexError:
            pass

    def update(self):
        try:
            if self.consulta_selecionada is None:
                self.view.exibir_mensagem("Selecione uma consulta da lista: ")
                return
            data_consulta, horario_consulta, observacoes = self.view.ler_dados_consulta()
            self.consulta_selecionada.atualizar_dados(horario_consulta, data_consulta, observacoes)
            self.consulta_dao.update(self.consulta_selecionada)
            self.get_all()
            self.view.exibir_mensagem("Consulta Atualizada com Sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {e}")

    def delete(self):
        if self.consulta_selecionada is None:
            self.view.exibir_mensagem("Seleciona uma consulta da lista: ")
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.consulta_dao.delete(self.consulta_selecionada.id)
            if sucesso:
                self.consulta_selecionada = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem("Consulta excluída com sucesso!")
            else:
                self.view.exibir_mensagem("Consulta não encontrada!")
        except Exception as e:
            self.view.exibir_mensagem("Erro ao excluir Consulta")