from app.models.vacina import Vacina


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
            self.view.exibir_mensagem("Vacina cadastrada com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

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
                self.view.exibir_mensagem("Selecione uma vacina na lista.", False)
                return
            nome, descricao = self.view.ler_dados_vacina()
            self.vacina_selecionada.atualizar_dados(nome, descricao)
            self.dao.update(self.vacina_selecionada)
            self.get_all()
            self.view.exibir_mensagem("Vacina atualizada com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def delete(self):
        if self.vacina_selecionada is None:
            self.view.exibir_mensagem("Selecione uma vacina na lista.", False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.vacina_selecionada.id)
            if sucesso:
                self.vacina_selecionada = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem("Vacina excluída com sucesso!")
            else:
                self.view.exibir_mensagem("Vacina não encontrada.", False)
        except Exception as e:
            self.view.exibir_mensagem("Problemas ao excluir vacina", False)