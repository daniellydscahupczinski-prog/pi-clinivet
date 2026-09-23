from app.models.animal import Animal
from app.core.data_utils import Data_Utils

from app.core.idiomas import Idioma
class Animal_Controller:

    def __init__(self, dao, cliente_dao, especie_dao, raca_dao, view):
        self.dao = dao
        self.view = view
        self.animal_selecionado = None
        self.cliente_dao = cliente_dao
        self.especie_dao = especie_dao
        self.raca_dao = raca_dao

    def new(self):
        self.view.limpar_campos()

    def save(self):
        try:
            nome, data_nascimento, sexo, peso, cliente_id, especie_id, raca_id = (
                self.view.ler_dados_animal()
            )

            animal = Animal(
                None,
                nome,
                Data_Utils.string_para_data(data_nascimento),
                sexo,
                peso,
                cliente_id,
                especie_id,
                raca_id
            )

            self.dao.save(animal)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("animal.cadastro"))

        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def carregar_clientes(self):
        cliente = self.cliente_dao.get_all()
        self.view.carregar_cliente(cliente)

    def carregar_especie(self):
        especie = self.especie_dao.get_all()
        self.view.carregar_especie(especie)

    def carregar_raca(self):
        raca = self.raca_dao.get_all()
        self.view.carregar_raca(raca)

    def get_all(self):
        animal = self.dao.get_all()
        self.view.exibir_animal(animal)

    def selecionar_animal(self, event):
        try:
            id_animal = self.view.get_id_selecionado()

            self.animal_selecionado = self.dao.get_by_id(
                id_animal
            )

            cliente = self.cliente_dao.get_all()

            especie = self.especie_dao.get_all()

            raca = self.raca_dao.get_all()

            self.view.preencher_campos(
                self.animal_selecionado,
                cliente, especie, raca
            )

        except IndexError:
            pass

    def update(self):
        try:
            if self.animal_selecionado is None:
                self.view.exibir_mensagem(
                    (Idioma.t("animal.selecionar_animal")),
                    False
                )
                return
            nome, data_nascimento, sexo, peso, cliente, especie, raca = (
                self.view.ler_dados_animal()
            )
            self.animal_selecionado.atualizar_dados(
                nome,
                Data_Utils.string_para_data(data_nascimento),
                sexo,
                peso,
                cliente,
                especie,
                raca
            )
            self.dao.update(self.animal_selecionado)
            self.get_all()
            self.view.exibir_mensagem(
                (Idioma.t("animal.atualizacao"))
            )
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def delete(self):
        if self.animal_selecionado is None:
            self.view.exibir_mensagem(
                (Idioma.t("animal.selecionar_animal")),
                False
            )
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(
                self.animal_selecionado.id
            )
            if sucesso:
                self.animal_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(
                    (Idioma.t("animal.exclusao"))
                )
            else:
                self.view.exibir_mensagem(
                    (Idioma.t("animal.nao_encontrado")),
                    False
                )
        except Exception:
            self.view.exibir_mensagem(
                (Idioma.t("animal.problema_exclusao")),
                False
            )