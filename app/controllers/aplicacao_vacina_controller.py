from app.models.aplicacao_vacina import Aplicacao_Vacina


class Aplicacao_Vacina_Controller:

    def __init__(self, dao, animal_dao, vacina_dao, view):
        self.dao = dao
        self.view = view
        self.aplicacao_vacina_selecionada = None
        self.animal_dao = animal_dao
        self.vacina_dao = vacina_dao

    def new(self):
        self.view.limpar_campos()
        self.aplicacao_vacina_selecionada = None

    def carregar_animal(self):
        animal = self.animal_dao.get_all()
        self.view.carregar_animal(animal)

    def carregar_vacina(self):
        vacina = self.vacina_dao.get_all()
        self.view.carregar_vacina(vacina)

    def save(self):
        try:
            tipo_servico, data_vacina, horario_vacina, status_vacina, animal_id, vacina_id = (
                self.view.ler_dados_aplicacao_vacina()
            )

            aplicacao_vacina = Aplicacao_Vacina(
                None,
                tipo_servico,
                data_vacina,
                horario_vacina,
                status_vacina,
                animal_id,
                vacina_id
            )

            self.dao.save(aplicacao_vacina)
            self.get_all()

            self.view.exibir_mensagem(
                "Aplicação da vacina cadastrada com sucesso!"
            )

        except ValueError as e:
            self.view.exibir_mensagem(
                "Erro: " + str(e),
                False
            )

    def get_all(self):
        aplicacoes_vacina = self.dao.get_all()
        self.view.exibir_aplicacoes_vacina(aplicacoes_vacina)

    def selecionar_aplicacoes_vacina(self, event):
        try:
            id_aplicacao_vacina = self.view.get_id_selecionado()

            self.aplicacao_vacina_selecionada = self.dao.get_by_id(
                id_aplicacao_vacina
            )

            self.view.preencher_campos(
                self.aplicacao_vacina_selecionada
            )

        except IndexError:
            pass

    def update(self):
        try:
            if self.aplicacao_vacina_selecionada is None:
                self.view.exibir_mensagem(
                    "Selecione uma aplicação da vacina na lista.",
                    False
                )
                return

            tipo_servico, data_vacina, horario_vacina, status_vacina, animal_id, vacina_id = (
                self.view.ler_dados_aplicacao_vacina()
            )

            self.aplicacao_vacina_selecionada.atualizar_dados(
                tipo_servico,
                data_vacina,
                horario_vacina,
                status_vacina,
                animal_id,
                vacina_id
            )

            self.dao.update(
                self.aplicacao_vacina_selecionada
            )

            self.get_all()

            self.view.exibir_mensagem(
                "Aplicação da vacina atualizada com sucesso!"
            )

        except ValueError as e:
            self.view.exibir_mensagem(
                "Erro: " + str(e),
                False
            )

    def delete(self):
        if self.aplicacao_vacina_selecionada is None:
            self.view.exibir_mensagem(
                "Selecione uma aplicação da vacina na lista.",
                False
            )
            return

        if not self.view.confirmar_exclusao():
            return

        try:
            sucesso = self.dao.delete(
                self.aplicacao_vacina_selecionada.id
            )

            if sucesso:
                self.aplicacao_vacina_selecionada = None
                self.view.limpar_campos()
                self.get_all()

                self.view.exibir_mensagem(
                    "Aplicação da vacina excluída com sucesso!"
                )

            else:
                self.view.exibir_mensagem(
                    "Aplicação da vacina não encontrada.",
                    False
                )

        except Exception:
            self.view.exibir_mensagem(
                "Problemas ao excluir a aplicação da vacina.",
                False
            )