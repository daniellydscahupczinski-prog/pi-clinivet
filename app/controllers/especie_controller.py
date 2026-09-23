from app.models.especie import Especie
from app.core.idiomas import Idioma 

class Especie_Controller:

    def __init__(self, dao, raca_dao, especie_raca_dao, view):
        self.dao = dao
        self.raca_dao = raca_dao
        self.especie_raca_dao = especie_raca_dao
        self.view = view
        self.especie_selecionada = None

    def new(self):
        self.view.limpar_campos()

    def save(self):
        try:
            nome = self.view.ler_dados_especie()
            raca = self.view.get_raca_selecionada()  # levanta ValueError se nada selecionado

            especie = Especie(None, nome)

            novo_id = self.dao.save(especie)
            # Só sobrescrevemos especie.id se o dao realmente retornar um
            # número (lastrowid). Se ele retornar outra coisa (ex: a própria
            # especie), confiamos que o dao já preencheu especie.id sozinho.
            if isinstance(novo_id, int):
                especie.id = novo_id

            self.especie_raca_dao.save(especie.id, raca.id)

            self.get_all()

            self.view.exibir_mensagem(
                Idioma.t("especie.cadastro")
            )

        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def get_all(self):
        especies = self.dao.get_all()
        self.view.exibir_especies(especies)

    def selecionar_especie(self, event=None):
        try:
            id_especie = self.view.get_id_selecionado()

            self.especie_selecionada = self.dao.get_by_id(
                id_especie
            )

            self.view.preencher_campos(
                self.especie_selecionada
            )

        except IndexError:
            pass

    def carregar_racas(self):
        racas = self.raca_dao.get_all()
        self.view.carregar_racas(racas)

    def update(self):
        try:
            if self.especie_selecionada is None:
                self.view.exibir_mensagem(
                    Idioma.t("especie.selecione_especie"),
                    False
                )
                return

            nome = self.view.ler_dados_especie()
            raca = self.view.get_raca_selecionada()

            self.especie_selecionada.atualizar_dados(
                self.especie_selecionada.id,
                nome
            )

            self.dao.update(
                self.especie_selecionada
            )

            self.especie_raca_dao.save(
                self.especie_selecionada.id,
                raca.id
            )

            self.get_all()

            self.view.exibir_mensagem(
                Idioma.t("especie.atualizada")
            )

        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def delete(self):
        if self.especie_selecionada is None:
            self.view.exibir_mensagem(
                Idioma.t("especie.selecione_especie"),
                False
            )
            return

        if not self.view.confirmar_exclusao():
            return

        try:
            sucesso = self.dao.delete(
                self.especie_selecionada.id
            )

            if sucesso:
                self.especie_selecionada = None
                self.view.limpar_campos()
                self.get_all()

                self.view.exibir_mensagem(
                    Idioma.t("especie.exclusao")
                )
            else:
                self.view.exibir_mensagem(
                    Idioma.t("especie.nao_encontrada"),
                    False
                )

        except Exception as e:
            self.view.exibir_mensagem(
                f"{Idioma.t("especie.problema_exclusao")}{Idioma.t(str(e))}",
                False
            )