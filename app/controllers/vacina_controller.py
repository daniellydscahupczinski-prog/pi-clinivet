from app.models.vacina import Vacina
from app.core.idiomas import Idioma 

class Vacina_Controller:
    def __init__(self, dao, view):
        self.dao = dao
        self.view = view
        self.vacina_selecionada = None 

    def new(self):
        self.view.limpar_campos()

    def save(self):
        try:
            nome, descricao = self.view.ler_dados_vacina()
            vacina = Vacina(
                None, 
                nome,
                descricao
            )
            self.dao.save(vacina)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("vacina.cadastro_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def get_all(self):
        vacina = self.dao.get_all()
        self.view.exibir_vacinas(vacina)

    def selecionar_vacina(self, event):
        try:
            id_vacina = self.view.get_id_selecionado()
            self.vacina_selecionada = self.dao.get_by_id(
                id_vacina
            )
            self.view.preencher_campos(
                self.vacina_selecionada
            )
        except IndexError:
            pass

    def update(self):
        try:
            if self.vacina_selecionada is None:
                self.view.exibir_mensagem(Idioma.t("vacina.selecionar_vacina"), False)
                return
            nome, descricao = self.view.ler_dados_vacina()
            self.vacina_selecionada.atualizar_dados(nome, descricao)
            self.dao.update(self.vacina_selecionada)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("vacina.atualizacao"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def delete(self):
        if self.vacina_selecionada is None:
            self.view.exibir_mensagem(Idioma.t("vacina.selecionar_vacina"), False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.vacina_selecionada.id)
            if sucesso:
                self.vacina_selecionada = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("vacina.exclusao"))
            else:
                self.view.exibir_mensagem(Idioma.t("vacina.nao_encontrada"), False)
        except Exception as e:
            self.view.exibir_mensagem(Idioma.t("vacina.problema_exclusao"), False)