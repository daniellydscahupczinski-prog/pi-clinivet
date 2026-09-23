from app.models.veterinario import Veterinario
from app.core.idiomas import Idioma


class Veterinario_Controller:

    def __init__(self, dao, view):
        self.dao = dao
        self.view = view
        self.veterinario_selecionado = None

    def new(self):
        self.view.limpar_campos()

    def save(self):
        try:
            nome, telefone, cpf, rg, especialidade = self.view.ler_dados_veterinario()

            veterinario = Veterinario(
                None,
                nome,
                cpf,
                telefone,
                rg,
                especialidade
            )

            self.dao.save(veterinario)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("veterinario.cadastro"))

        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def get_all(self):
        veterinarios = self.dao.get_all()
        self.view.exibir_veterinarios(veterinarios)

    def selecionar_veterinario(self, event):
        try:
            veterinario_id = self.view.get_id_selecionado()

            self.veterinario_selecionado = self.dao.get_by_id(
                veterinario_id
            )

            self.view.preencher_campos(
                self.veterinario_selecionado
            )

        except IndexError:
            pass

    def update(self):
        try:
            if self.veterinario_selecionado is None:
                self.view.exibir_mensagem(Idioma.t("veterinario.selecione_veterinario"), False)
                return

            nome, telefone, cpf, rg, especialidade = self.view.ler_dados_veterinario()

            self.veterinario_selecionado.atualizar_dados(
                self.veterinario_selecionado.id,
                nome,
                cpf,
                rg,
                telefone,
                especialidade
            )

            self.dao.update(self.veterinario_selecionado)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("veterinario.atualizacao"))

        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def delete(self):
        if self.veterinario_selecionado is None:
            self.view.exibir_mensagem(Idioma.t("veterinario.selecione_veterinario"), False)
            return

        if not self.view.confirmar_exclusao():
            return

        try:
            sucesso = self.dao.delete(self.veterinario_selecionado.id)

            if sucesso:
                self.veterinario_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("veterinario.exclusao"))
            else:
                self.view.exibir_mensagem(Idioma.t("veterinario.nao_encontrado"), False)

        except Exception as e:
            self.view.exibir_mensagem(Idioma.t("veterinario.erro_exclusao"), False)

    def fechar(self):
        self.view.fechar()