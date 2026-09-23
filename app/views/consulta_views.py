from app.models.consulta import Consulta
import tkinter as tk
from  tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry

from app.core.idiomas import Idioma

class Consulta_View:
    def __init__(self,root,controller):
        self.root = root
        self.veterinarios = []
        self.controller = controller
       
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title(Idioma.t("consulta.janela_titulo"))
        self.root.geometry("800x600")
        self.root.resizable(False,False)

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = (Idioma.t("consulta.titulo")),
            font = ("Arial", 16, "bold"),
        )
        self.lbl_titulo.grid(
            row = 0,
            column = 0,
            columnspan = 4,
            padx = 5, 
            pady = 5
        )
        self.frm_dados = tk.LabelFrame(
            self.root, 
            text = (Idioma.t("consulta.dados"))
        )
        self.frm_dados.grid(
            row = 1, 
            column = 0,
            columnspan = 4, 
            padx = 10, 
            pady = 5, 
            sticky = "ew"
        )
        self.frm_dados.grid_columnconfigure(0,weight = 0)
        self.frm_dados.grid_columnconfigure(1, weight = 1)
        self.frm_dados.grid_columnconfigure(2, weight = 2)
        self.frm_dados.grid_columnconfigure(3, weight = 3)
        self.lbl_id = tk.Label(
            self.frm_dados, 
            text = (Idioma.t("comum.id"))
        )
        self.lbl_id.grid(
            row =0,
            column = 0,
            padx = 5, 
            pady = 5,
            sticky = "w"

        )
        self.txt_id = tk.Entry(
            self.frm_dados,
            width = 10, 
            state = "readonly"
        )
        self.txt_id.grid(
            row = 0, 
            column = 1, 
            padx = 5, 
            pady = 5,
            sticky = "w"
        )
        self.lbl_data_consulta = tk.Label(
            self.frm_dados, 
            text = ("DATA CONSULTA")
        )
        self.lbl_data_consulta.grid(
            row = 1, 
            column = 0, 
            padx = 5, 
            pady = 5, 
            sticky = "w"
        )
        self.txt_data_consulta = DateEntry(
            self.frm_dados, 
            width = 40,
            date_pattern="dd/mm/yyyy"
        )
        self.txt_data_consulta.grid(
            row = 1, 
            column = 1, 
            padx = 5, 
            pady =5, 
            sticky ="w"
        )
        self.lbl_horario_consulta = tk.Label(
            self.frm_dados, 
            text = (Idioma.t("consulta.horario"))
        )
        self.lbl_horario_consulta.grid(
            row = 2, 
            column = 0, 
            padx = 5, 
            pady = 5,
            sticky = "w"
        )
        self.cmb_horario_consulta = ttk.Combobox(
            self.frm_dados,
            width=37,
            state="readonly",
            values=[
                "08:00",
                "09:00",
                "10:00",
                "11:00",
                "14:00",
                "15:00",
                "16:00"
            ]
        )
        
        self.cmb_horario_consulta.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.lbl_observacoes = tk.Label(
            self.frm_dados, 
            text = (Idioma.t("consulta.observacao"))
        )
        self.lbl_observacoes.grid(
            row = 3, 
            column = 0, 
            padx = 5, 
            pady = 5, 
            sticky = "w"
        )
        self.txt_observacoes = tk.Entry(
            self.frm_dados, 
            width = 20
        )
        self.txt_observacoes.grid(
            row = 3, 
            column = 1,
            padx = 5, 
            pady =5, 
            sticky = "w"
        )
        self.lbl_veterinario = tk.Label(
            self.frm_dados,
            text=(Idioma.t("consulta.veterinario"))
        )

        self.lbl_veterinario.grid(
            row=4,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.cmb_veterinario = ttk.Combobox(
            self.frm_dados,
            width=37,
            state="readonly"
        )

        self.cmb_veterinario.grid(
            row=4,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.frm_botoes = tk.Frame(
            self.frm_dados,
            border = 2,
            relief = "groove"
        )
        self.frm_botoes.grid(
            row = 5,
            column = 0,
            padx = 10,
            pady = 5,
            columnspan = 4,
        )
        self.btn_novo = tk.Button(
            self.frm_botoes,
            text=(Idioma.t("comum.novo")),
            width=15
        )
        self.btn_novo.grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )
        self.btn_salvar = tk.Button(
            self.frm_botoes,
            text=(Idioma.t("comum.salvar")),
            width=15
        )
        self.btn_salvar.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )
        self.btn_alterar = tk.Button(
            self.frm_botoes,
            text=(Idioma.t("comum.alterar")),
            width=15
        )
        self.btn_alterar.grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )
        self.btn_excluir = tk.Button(
            self.frm_botoes,
            text=(Idioma.t("comum.excluir")),
            width=15
        )
        self.btn_excluir.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )
        self.btn_fechar = tk.Button(
            self.frm_botoes,
            text=(Idioma.t("comum.fechar")),
            width=15
        )
        self.btn_fechar.grid(
            row=0,
            column=4,
            padx=5,
            pady=5
        )

        self.tbl_consulta = ttk.Treeview(
            self.root,
            show="headings"
        )
    def configurar_treeview(self):
        self.tbl_consulta["columns"]=(
            "id",
            "data_consulta",
            "horario_consulta",
            "observacoes",
            "veterinario"
        )
        self.tbl_consulta.column(
            "#0",
            width = 0, 
            stretch = False
        )
        self.tbl_consulta.column(
            "id",
            width = 50, 
            anchor = "center"
        )
        self.tbl_consulta.column(
            "data_consulta", 
            width = 150,

        )
        self.tbl_consulta.column(
            "horario_consulta",
            width = 150
        )
        self.tbl_consulta.column(
            "observacoes",
            width = 300

        )
        self.tbl_consulta.column(
             "veterinario", 
             width = 150
        )
        self.tbl_consulta.heading(
            "id",
            text = (Idioma.t("comum.id"))
        )
        self.tbl_consulta.heading(
            "data_consulta",
            text = (Idioma.t("consulta.data"))
        )
        self.tbl_consulta.heading(
            "horario_consulta",
            text = (Idioma.t("consulta.horario"))
        )
        self.tbl_consulta.heading(
            "observacoes",
            text = (Idioma.t("consulta.observacao"))
        )
        self.tbl_consulta.heading(
             "veterinario",
             text = (Idioma.t("consulta.veterinario"))
        )
    def configurar_eventos(self):
        self.btn_novo.config(
            command = self.controller.new
        )   
        self.btn_salvar.config(
            command = self.controller.save
        )
        self.btn_alterar.config(
            command = self.controller.update
        )
        self.btn_excluir.config(
            command = self.controller.delete
        )
        self.btn_fechar.config(
            command = self.fechar
        )
        self.tbl_consulta.grid(
            row=2,
            column=0,
            columnspan=4,
            padx=10,
            pady=10,
            sticky="nsew")
        
        self.tbl_consulta.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_consulta
        )
    def preencher_campos(self,consulta):
            self.limpar_campos()
            self.txt_id.config(state = "normal")
            self.txt_id.insert(
                0, 
                str(consulta.id)

            )
            self.txt_id.config(state = "readonly")
            self.txt_data_consulta.insert(
                0, 
                consulta.data_consulta
            )
            self.cmb_horario_consulta.insert(
                0, 
                consulta.horario_consulta
            )
            self.txt_observacoes.insert(
                0, 
                consulta.observacoes
            )
    def limpar_campos(self):
            self.txt_id.config(state = "normal")
            self.txt_id.delete(0,tk.END)
            self.txt_id.config(state = "readonly")
            self.txt_data_consulta.delete(0,tk.END)
            self.cmb_horario_consulta.delete(0,tk.END)
            self.txt_observacoes.delete(0, tk.END)
            self.cmb_veterinario.delete(0, tk.END)
    def limpar_treeview(self):
         for item in self.tbl_consulta.get_children():
              self.tbl_consulta.delete(item)
    def get_id_selecionado(self):
         item = self.tbl_consulta.selection()[0]
         return self.tbl_consulta.item(item)["values"][0]
    def confirmar_exclusao(self):
         
         return messagebox.askyesno(
              (Idioma.t("comum.confirmacao")),
              (Idioma.t("consulta.confirmacao_exclusao")),
              parent= self.root
         )
    def ler_dados_consulta(self):
         data_consulta = self.txt_data_consulta.get()
         horario_consulta = self.cmb_horario_consulta.get()
         observacoes = self.txt_observacoes.get()
         return data_consulta, horario_consulta, observacoes
    def carregar_veterinarios(self, veterinarios):
        self.veterinarios = veterinarios

        self.cmb_veterinario["values"] = [
        veterinario.nome for veterinario in veterinarios
    ]
        
    def get_veterinario_selecionado(self):
        indice = self.cmb_veterinario.current()

        if indice == -1:
            return None

        return self.veterinarios[indice]
    def carregar_veterinarios(self, veterinarios):
        self.veterinarios = veterinarios

        self.cmb_veterinario["values"] = [
            veterinario.nome
            for veterinario in veterinarios
        ]
    
        

    def exibir_mensagem(self, mensagem, sucesso = True):
         if sucesso: 
              messagebox.showinfo(
                   "CliniVet", 
                   mensagem, 
                   parent=self.root
              )
         else: 
              messagebox.showerror(
                   "CliniVet",
                   mensagem, 
                   parent=self.root
              )
    def exibir_consulta(self, consultas):

        self.limpar_treeview()

        for consulta in consultas:
            self.tbl_consulta.insert(
                "",
                tk.END,
                values=(
                    consulta.id,
                    consulta.data_consulta,
                    consulta.horario_consulta,
                    consulta.observacoes,
                    consulta.veterinario
                )
            )
    def fechar(self): 
         self.root.destroy()

    def iniciar(self):
        self.controller.carregar_veterinarios()
        self.controller.get_all()