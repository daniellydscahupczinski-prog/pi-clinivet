from app.models.raca import Raca

class Raca_Controller:

    def __init__(
        self,
        dao,
        view
    ):
        self.dao = dao
        self.view = view
        self.raca_selecionada = None

    def new(self):
        self.view.limpar_campos()

    def save(self):
        try:
            nome = self.view.ler_dados_raca()
            raca = Raca(
                None,
                nome
            )
            self.dao.save(raca)
            self.get_all()
            self.view.exibir_mensagem((("Raca cadastrada com sucesso!")))
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def get_all(self):
        raca = self.dao.get_all()
        self.view.exibir_racas(raca)

    def selecionar_raca(self, event):
        try:
            id_raca = self.view.get_id_selecionado()
            self.raca_selecionada = self.dao.get_by_id(
                id_raca
            )

            self.view.preencher_campos(
                self.raca_selecionada
            )

        except IndexError:
            pass

    def update(self):
        try:
            if self.raca_selecionada is None:
                self.view.exibir_mensagem("Selecione uma raca da lista", False)
                return
            nome = self.view.ler_dados_raca()
            self.raca_selecionada.atualizar_dados(nome)
            self.dao.update(self.raca_selecionada)
            self.get_all()
            self.view.exibir_mensagem((("raca atualizada")))
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def delete(self):
        if self.raca_selecionada is None:
            self.view.exibir_mensagem("Selecione uma raca na lista", False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.raca_selecionada.id)
            if sucesso:
                self.raca_selecionada = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem((("raca excluida com sucesso")))
            else:
                self.view.exibir_mensagem("Raca nao encontrada", False)
        except Exception as e:
            self.view.exibir_mensagem("Problemas ao excluir raca", False)