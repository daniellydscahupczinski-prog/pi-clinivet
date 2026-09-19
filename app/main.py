from app.core.database import Database
import tkinter as tk
from colorama import init

from app.dao.veterinario_dao import Veterinario_DAO
from app.views.veterinario_view import Veterinario_View
from app.controllers.veterinario_controller import Veterinario_Controller

from app.dao.consulta_dao import Consulta_DAO
from app.dao.consulta_veterinario_dao import Consulta_Veterinario_DAO
from app.views.consulta_views import Consulta_View
from app.controllers.consulta_controller import Consulta_Controller


from app.dao.especie_dao import Especie_DAO
from app.dao.especie_raca_dao import Especie_Raca_DAO
from app.views.especie_views import Especie_View
from app.controllers.especie_controller import Especie_Controller

from app.dao.raca_dao import Raca_DAO

class ErpApplication:

    def __init__(self):

        init(autoreset=True)

        self._database = Database()

        self._root = tk.Tk()

        self._janela_consulta = None
        self._janela_veterinario = None
        self._janela_especie = None


        self._configurar_janela()

        self._dao_consulta = Consulta_DAO(
            self._database
        )
        self._dao_consulta_veterinario = Consulta_Veterinario_DAO(
            self._database
        )
        self._ctrl_consulta = Consulta_Controller(
            dao = self._dao_consulta,
            veterinario_dao = self._dao_veterinario,
            consulta_vaterinario_dao = self._dao_consulta_veterinario,
            view = None
        )
        self._dao_veterinario = Veterinario_DAO(
            self._database
        )
        self._ctrl_veterinario = Veterinario_Controller(
            dao = self._dao_veterinario,
            view = None
        )
        self._dao_especie = Especie_DAO(
            self._database
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
        self._criar_menu()

    def _configurar_janela(self):
        self._root.title("Sistema Corporativo CliniVet")
        self._root.state("zoomed")  
    def _criar_menu(self):

        menu_principal = tk.Menu(self._root) 
        menu_cadastros_basicos = tk.Menu(menu_principal, tearoff=0) 
        
        menu_cadastros_basicos.add_command(
            label = "Especie",
            command = self._abrir_especie

        )
        menu_principal.add_cascade(
            label="Cadastros básicos",
            menu=menu_cadastros_basicos
        )
        menu_acessos = tk.Menu(menu_principal, tearoff=0)
        menu_acessos.add_command(
            label="consulta",
            command = self._abrir_consulta
        )
        menu_acessos.add_command(
            label="veterinarios",
            command = self._abrir_veterinario
        )
        menu_principal.add_cascade(
            label="Acessos",
            menu=menu_acessos
        )
        menu_principal.add_command(
            label="Sair",

            command=self._root.destroy
        )

        self._root.config(menu=menu_principal)

    def _abrir_janela(self, atributo_janela, classe_view, controller):

        janela_existente = getattr(self, atributo_janela)

        if janela_existente is not None and janela_existente.winfo_exists():
            janela_existente.lift()
            janela_existente.focus_force()
            return

        janela = tk.Toplevel(self._root)
        setattr(self, atributo_janela, janela)

        controller.view = classe_view(janela, controller)
        controller.view.iniciar()       

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
        
    if __name__ =="__main__":

        app = ErpApplication()



