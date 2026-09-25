
from colorama import init, Fore, Style
from app.core.database import Database
from app.views.home_view import Home_View
from app.core.idiomas import Idioma
 
# Componentes de Raca
from app.dao.raca_dao import Raca_DAO
from app.views.raca_views import Raca_View
from app.controllers.raca_controller import Raca_Controller
 
# Componentes de Cliente
from app.dao.cliente_dao import Cliente_DAO
from app.dao.animal_dao import Animal_DAO
from app.views.cliente_views import Cliente_View
from app.controllers.cliente_controller import Cliente_Controller
 
# Componentes de Agendamento
from app.dao.agendamento_dao import Agendamento_DAO
from app.views.agendamento_views import Agendamento_View
from app.controllers.agendamento_controller import Agendamento_Controller
from app.views.agenda_dia_views import Agenda_Dia_View
 
# Componentes de Animal
from app.dao.animal_dao import Animal_DAO
from app.views.animal_views import Animal_View
from app.controllers.animal_controller import Animal_Controller
 
# Componentes de Vacina
from app.dao.vacina_dao import Vacina_DAO
from app.views.vacina_views import Vacina_View
from app.controllers.vacina_controller import Vacina_Controller
 
# Componentes de Aplicacao_vacina
from app.dao.aplicacao_vacina_dao import Aplicacao_Vacina_DAO
from app.views.aplicacao_vacina_views import Aplicacao_Vacina_View
from app.controllers.aplicacao_vacina_controller import Aplicacao_Vacina_Controller
 
# Componentes de Animal
from app.dao.animal_dao import Animal_DAO
from app.views.animal_views import Animal_View
from app.controllers.animal_controller import Animal_Controller
 
# Componentes de Vacina
from app.dao.vacina_dao import Vacina_DAO
from app.views.vacina_views import Vacina_View
from app.controllers.vacina_controller import Vacina_Controller
 
# Componentes de Aplicacao_Vacina
from app.dao.aplicacao_vacina_dao import Aplicacao_Vacina_DAO
from app.views.aplicacao_vacina_views import Aplicacao_Vacina_View
from app.controllers.aplicacao_vacina_controller import Aplicacao_Vacina_Controller
 
from app.dao.veterinario_dao import Veterinario_DAO
from app.views.veterinario_views import Veterinario_View
from app.controllers.veterinario_controller import Veterinario_Controller
 
from app.dao.consulta_dao import Consulta_DAO
from app.dao.consulta_veterinario_dao import Consulta_Veterinario_DAO
from app.views.consulta_views import Consulta_View
from app.controllers.consulta_controller import Consulta_Controller
 
from app.dao.especie_dao import Especie_DAO
from app.dao.especie_raca_dao import Especie_Raca_DAO
from app.views.especie_views import Especie_View
from app.controllers.especie_controller import Especie_Controller
 
 
import tkinter as tk
from PIL import Image, ImageTk


class ErpApplication:
 
    def __init__(self):
        init(autoreset=True)
 
        self._database = Database()
        self._root = tk.Tk()
 
        self._usuario_logado = None
 
        self._janela_raca = None
        self._janela_agendamento = None
        self._janela_cliente = None
        self._janela_animal = None
        self._janela_vacina = None
        self._janela_aplicacao_vacina = None
        self._janela_agenda_dia = None
        self._janela_consulta = None
        self._janela_veterinario = None
        self._janela_especie = None

        
        self._img_marca_dagua = None
        self._label_marca_dagua = None

        # ================================
        # RACA
        # ================================
        self._dao_raca = Raca_DAO(
            self._database
        )
        self._dao_especie = Especie_DAO(
            self._database
        )
        self._ctrl_raca = Raca_Controller(
            dao=self._dao_raca,
            view=None
        )
 
        # ==================================
        # CLIENTE (precisa estar antes do ANIMAL)
        # =================================
        self._dao_animal = Animal_DAO(
            self._database
        )
        self._dao_cliente = Cliente_DAO(
            self._database
        )
        self._ctrl_cliente = Cliente_Controller(
            dao=self._dao_cliente,
            view=None
        )
 
        # ==================================
        # ANIMAL
        # ==================================
        self._ctrl_animal = Animal_Controller(
            dao=self._dao_animal,
            cliente_dao=self._dao_cliente,
            especie_dao=self._dao_especie,
            raca_dao=self._dao_raca,
            view=None
        )
 
        # ==================================
        # AGENDAMENTO
        # ==================================
        self._dao_agendamento = Agendamento_DAO(
            self._database
        )
        self._ctrl_agendamento = Agendamento_Controller(
            dao=self._dao_agendamento,
            view=None
        )
 
        # ==================================
        # VACINA
        # ==================================
        self._dao_vacina = Vacina_DAO(
            self._database
        )
        self._ctrl_vacina = Vacina_Controller(
            dao=self._dao_vacina,
            view=None
        )
 
        # ==================================
        # APLICACAO_VACINA
        # ==================================
        self._dao_animal = Animal_DAO(
            self._database
        )
        self._dao_vacina = Vacina_DAO(
            self._database
        )
        self._dao_aplicacao_vacina = Aplicacao_Vacina_DAO(
            self._database
        )
        self._ctrl_aplicacao_vacina = Aplicacao_Vacina_Controller(
            dao=self._dao_aplicacao_vacina,
            animal_dao=self._dao_animal,
            vacina_dao=self._dao_vacina,
            view=None
        )

        # ==================================
        # CONSULTA
        # ==================================
        self._dao_consulta = Consulta_DAO(
            self._database
        )
        self._dao_consulta_veterinario = Consulta_Veterinario_DAO(
            self._database
        )
        self._dao_veterinario = Veterinario_DAO(
            self._database
        )
        self._ctrl_consulta = Consulta_Controller(
            consulta_dao = self._dao_consulta,
            veterinario_dao = self._dao_veterinario,
            consulta_veterinario_dao = self._dao_consulta_veterinario,
            view = None
        )

        # ==================================
        # VETERINÁRIO
        # ==================================
        self._ctrl_veterinario = Veterinario_Controller(
            dao = self._dao_veterinario,
            view = None
        )
        self._dao_especie_raca= Especie_Raca_DAO(
            self._database
        )
        self._ctrl_especie = Especie_Controller(
            dao = self._dao_especie,
            raca_dao = self._dao_raca,
            especie_raca_dao = self._dao_especie_raca,
            view = None
        )
        self._home_view = Home_View(
            self._root,
            self
        )
 
        self._configurar_janela()
        self._criar_menu()
        self._adicionar_marca_dagua()

    def _configurar_janela(self):
        titulo = (Idioma.t("home_view.janela"))
 
        if self._usuario_logado is not None:
            titulo = f"{titulo} — {self._usuario_logado.nome} ({self._usuario_logado.perfil.nome})"
 
        self._root.title(titulo)
        self._root.state("zoomed")
        self._root.configure(bg="#FFFCF5")

    def _adicionar_marca_dagua(self):
        """
        Coloca a imagem app/assets/watermark_clinivet_original.png como marca
        d'água no canto inferior direito da janela principal, atrás de
        qualquer outro conteúdo que venha a ser adicionado ao self._root.

        Essa versão usa a imagem original (com o fundo creme #FFFCF5 dela),
        por isso o fundo do self._root também está configurado com a mesma
        cor em _configurar_janela — assim não fica um "quadrado" destacado
        ao redor da imagem.
        """
        caminho_imagem = "app/assets/watermark_clinivet_original.png"

        try:
            img = Image.open(caminho_imagem).convert("RGB")
        except FileNotFoundError:
            print(
                Fore.YELLOW
                + f"[Aviso] Marca d'água não encontrada em '{caminho_imagem}'. "
                  "Pulei essa etapa."
            )
            return

        # Redimensiona mantendo a proporção 
        largura = 380
        proporcao = largura / img.width
        altura = int(img.height * proporcao)
        img = img.resize((largura, altura), Image.LANCZOS)

        self._img_marca_dagua = ImageTk.PhotoImage(img)

        self._label_marca_dagua = tk.Label(
            self._root,
            image=self._img_marca_dagua,
            bg="#FFFCF5",
            bd=0
        )
       
        self._label_marca_dagua.place(
            relx=1.0, rely=1.0, anchor="se", x=-30, y=-30
        )
        self._label_marca_dagua.lower()

    def _criar_menu(self):
    
        menu_principal = tk.Menu(self._root)
 
        menu_cadastros_basicos = tk.Menu(menu_principal, tearoff=0)
 
        menu_cadastros_basicos.add_command(
            label=(Idioma.t("menu.raca")),
            command=self._abrir_raca
        )
 
        menu_cadastros_basicos.add_command(
            label=(Idioma.t("menu.cliente")),
            command=self._abrir_cliente
        )
 
        menu_cadastros_basicos.add_command(
            label=(Idioma.t("menu.agendamento")),
            command=self._abrir_agendamento
        )
 
        menu_cadastros_basicos.add_command(
            label=(Idioma.t("menu.animal")),
            command=self._abrir_animal
        )
 
        menu_cadastros_basicos.add_command(
            label=(Idioma.t("menu.vacina")),
            command=self._abrir_vacina
        )
 
        menu_cadastros_basicos.add_command(
            label=(Idioma.t("menu.aplicacao_vacina")),
            command=self._abrir_aplicacao_vacina
        )
 
        menu_cadastros_basicos.add_command(
            label = (Idioma.t("menu.especie")),
            command = self._abrir_especie
        )
 
        menu_acessos = tk.Menu(menu_principal, tearoff=0)
        menu_acessos.add_command(
            label=(Idioma.t("menu.consulta")),
            command = self._abrir_consulta
        )
        menu_acessos.add_command(
            label=(Idioma.t( "menu.veterinario")),
            command = self._abrir_veterinario
        )

        # ===========================
        # IDIOMA
        # ===========================

        menu_idioma = tk.Menu(
            menu_principal,
            tearoff=0
        )

        menu_idioma.add_command(
            label="Português",
            command=self._selecionar_portugues
        )

        menu_idioma.add_command(
            label="English",
            command=self._selecionar_ingles
        )

        menu_principal.add_cascade(
            label=Idioma.t("menu.idioma"),
            menu=menu_idioma
        )

        self._root.config(menu=menu_principal)
 
    # ===========================
    # IDIOMA
    # ===========================

    def _mudar_idioma(self, codigo):

        Idioma.definir(
            codigo
        )
        self._criar_menu()

    def _selecionar_portugues(self):

        self._mudar_idioma(
            "pt"
        )
    def _selecionar_ingles(self):

        self._mudar_idioma(
            "en"
        )
 
    def _popup_menu(self, menu):
        """Exibe um tk.Menu na posição atual do ponteiro do mouse."""
        x = self._root.winfo_pointerx()
        y = self._root.winfo_pointery()
 
        try:
            menu.tk_popup(x, y)
        finally:
            menu.grab_release()
 
    def abrir_cadastros(self):
        """Botão 'Cadastros Básicos': os 7 cadastros básicos."""
        menu = tk.Menu(self._root, tearoff=0)
 
        menu.add_command(label=(Idioma.t("menu.raca")), command=self._abrir_raca)
        menu.add_command(label=(Idioma.t("menu.cliente")), command=self._abrir_cliente)
        menu.add_command(label=(Idioma.t("menu.agendamento")), command=self._abrir_agendamento)
        menu.add_command(label=(Idioma.t("menu.animal")), command=self._abrir_animal)
        menu.add_command(label=(Idioma.t("menu.vacina")), command=self._abrir_vacina)
        menu.add_command(label=(Idioma.t("menu.aplicacao_vacina")), command=self._abrir_aplicacao_vacina)
        menu.add_command(label=(Idioma.t("menu.especie")), command=self._abrir_especie)
 
        self._popup_menu(menu)
 
    def abrir_menus(self):
        """Botão 'Menus': tudo junto (cadastros + agenda + acessos)."""
        menu = tk.Menu(self._root, tearoff=0)
 
        menu.add_command(label=(Idioma.t("menu.raca")), command=self._abrir_raca)
        menu.add_command(label=(Idioma.t("menu.cliente")), command=self._abrir_cliente)
        menu.add_command(label=(Idioma.t("menu.agendamento")), command=self._abrir_agendamento)
        menu.add_command(label=(Idioma.t("menu.animal")), command=self._abrir_animal)
        menu.add_command(label=(Idioma.t("menu.vacina")), command=self._abrir_vacina)
        menu.add_command(label=(Idioma.t("menu.aplicacao_vacina")), command=self._abrir_aplicacao_vacina)
        menu.add_command(label=(Idioma.t("menu.especie")), command=self._abrir_especie)
 
        menu.add_separator()
        menu.add_command(label=(Idioma.t("agenda.agenda_dia")), command=self._abrir_agenda_dia)
 
        menu.add_separator()
        menu.add_command(label=(Idioma.t("menu.consulta")), command=self._abrir_consulta)
        menu.add_command(label=(Idioma.t("menu.veterinario")), command=self._abrir_veterinario)
 
        self._popup_menu(menu)
 
    def abrir_acessos(self):
        menu = tk.Menu(self._root, tearoff=0)
 
        menu.add_command(label=(Idioma.t("menu.consulta")), command=self._abrir_consulta)
        menu.add_command(label=(Idioma.t("menu.veterinario")), command=self._abrir_veterinario)
 
        self._popup_menu(menu)
 
    def sair(self):
        self._root.destroy()
 
    def _abrir_janela(
        self,
        atributo_janela,
        classe_view,
        controller
    ):
        janela_existente = getattr(
            self,
            atributo_janela
        )
 
        if (
            janela_existente is not None
            and janela_existente.winfo_exists()
        ):
            janela_existente.lift()
            janela_existente.focus_force()
            return
 
        janela = tk.Toplevel(
            self._root
        )
 
        setattr(
            self,
            atributo_janela,
            janela
        )
 
        controller.view = classe_view(
            janela,
            controller
        )
 
        controller.view.iniciar()
 
    def _abrir_raca(self):
        self._abrir_janela(
            "_janela_raca",
            Raca_View,
            self._ctrl_raca
        )
 
    def _abrir_cliente(self):
        self._abrir_janela(
            "_janela_cliente",
            Cliente_View,
            self._ctrl_cliente
        )
 
    def _abrir_agendamento(self):
        self._abrir_janela(
            "_janela_agendamento",
            Agendamento_View,
            self._ctrl_agendamento
        )
 
    def _abrir_animal(self):
        self._abrir_janela(
            "_janela_animal",
            Animal_View,
            self._ctrl_animal
        )
 
    def _abrir_vacina(self):
        self._abrir_janela(
            "_janela_vacina",
            Vacina_View,
            self._ctrl_vacina
        )
 
    def _abrir_aplicacao_vacina(self):
        self._abrir_janela(
            "_janela_aplicacao_vacina",
            Aplicacao_Vacina_View,
            self._ctrl_aplicacao_vacina
        )
 
    def _abrir_agenda_dia(self):
        if (
            self._janela_agenda_dia is not None
            and self._janela_agenda_dia.winfo_exists()
        ):
            self._janela_agenda_dia.lift()
            self._janela_agenda_dia.focus_force()
            return
 
        self._janela_agenda_dia = tk.Toplevel(
            self._root
        )
 
        Agenda_Dia_View(
            self._janela_agenda_dia,
            self._dao_agendamento
        )
 
    def _abrir_consulta(self):
        self._abrir_janela("_janela_consulta", Consulta_View,
                           self._ctrl_consulta)
    def _abrir_veterinario(self):
        self._abrir_janela("_janela_veterinario", Veterinario_View,
                           self._ctrl_veterinario)
    def _abrir_especie(self):
        self._abrir_janela("_janela_especie", Especie_View, 
                           self._ctrl_especie)
 
    def run(self):
        self._root.mainloop()
 
 
if __name__ == "__main__":
    app = ErpApplication()
    app.run()