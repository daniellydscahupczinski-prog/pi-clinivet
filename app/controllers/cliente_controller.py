from app.models.cliente import Cliente

class Cliente_Controller:
    def __init__(self, dao, view):
        self.dao = dao
        self.view = view
        self.cliente_selecionada = None

    def new(self):
        self.view.limpar_campos()

    def save(self):
        try:
            nome, telefone, cpf = self.view.ler_dados_cliente()

            cliente = Cliente(
                None,
                nome,
                telefone,
                cpf
            )

            self.dao.save(cliente)
            self.get_all()
            self.view.exibir_mensagem("Cliente cadastrado com sucesso!")

        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def get_all(self):
        cliente = self.dao.get_all()
        self.view.exibir_cliente(cliente)

    def selecionar_cliente(self, event):
        try:
            id_cliente = self.view.get_id_selecionado()

            self.cliente_selecionada = self.dao.get_by_id(
                id_cliente
            )

            self.view.preencher_campos(
                self.cliente_selecionada
            )

        except IndexError:
            pass

    def update(self):
        try:
            if self.cliente_selecionada is None:
                self.view.exibir_mensagem("selecione um cliente", False)
                return

            nome, telefone, cpf = self.view.ler_dados_cliente()

            self.cliente_selecionada.atualizar_dados(
                nome,
                telefone,
                cpf
            )

            self.dao.update(self.cliente_selecionada)
            self.get_all()
            self.view.exibir_mensagem("Cliente atualizado!")

        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def delete(self):
        if self.cliente_selecionada is None:
            self.view.exibir_mensagem("Selecione um cliente", False)
            return

        if not self.view.confirmar_exclusao():
            return

        try:
            sucesso = self.dao.delete(
                self.cliente_selecionada.id
            )

            if sucesso:
                self.cliente_selecionada = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(
                    "Cliente excluido com sucesso!"
                )

            else:
                self.view.exibir_mensagem(
                    "Nenhum cliente encontrado!",
                    False
                )

        except Exception as e:
            self.view.exibir_mensagem(
                "Problemas ao excluir cliente!!",
                False
            )