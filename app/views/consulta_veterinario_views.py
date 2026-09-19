import tkinter as tk 
from tkinter import messagebox

class Consulta_veterinario_View: 
    def __init__(
            self, 
            root, 
            controller, 
            consulta, 
            veterinario
    ):
        self.root = root
        self.controller = controller
        self.consulta = consulta
        self.veterinarios = veterinario

        self.configurar_janela()
        self.criar_componentes()
        self.preencher_lista()

    def configurar_janela(self):
        self.root.title(f"Veterinarios disponíveis para consulta.")
        self.root.geometry("400x450")
        self.root.resizable(False,False)

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root, 
            text = f"Veterinarios Disponiveis para consulta. ",
            font = ("Arial", 12, "bold"),
            wraplength = 380
        )
        self.lbl_titulo.pack(
            padx = 10, 
            pady = 10
        )
        self.lbl_instrucao = tk.Label(
            self.root, 
            text = "Clique para selecionar/desmarcar veterinario desejado. "
        )
        self.lbl_instrucao.pack(
            padx = 10, 
            anchor = "w"
        )
        self.lst_veterinario = tk.Listbox(
            self.root, 
            selectmode = tk.SINGLE, 
            height = 15

        )
        self.lst_veterinario.pack(
            padx = 10,
            pady = 10, 
            fill = "both",
            expand = True
        )
        self.frm_botoes = tk.Frame(
            self.root
        )
        self.frm_botoes.pack(
            pady = 10
        )
        self.btn_salvar = tk.Button(
            self.frm_botoes, 
            text = "Salvar", 
            width = 15, 
            command = self.salvar
        )
        self.btn_salvar.grid(
            row = 0, 
            column = 0, 
            padx =5
        )
        self.btn_cancelar = tk.Button(
            self.frm_botoes, 
            text = "Cancelar",
            width = 15, 
            command = self.fechar
        )
        self.btn_cancelar.grid(
            row = 0, 
            column = 1, 
            padx = 5
        )
    def preencher_lista(self):

        veterinario_associado = self.consulta.veterinario

        for indice, veterinario in enumerate(self.veterinarios):
            self.lst_veterinario.insert(
                tk.END,
                veterinario.nome
            )

            if veterinario.id == veterinario_associado.id:
                self.lst_veterinario.selection_set(indice)

    def salvar(self):

        indices_selecionados = self.lst_veterinario.curselection()

        if not indices_selecionados:
            self.exibir_mensagem(
                "Selecione um veterinário!",
                False
            )
            return

        indice = indices_selecionados[0]

        veterinario_selecionado = self.veterinarios[indice]

        self.controller.salvar_veterinario(
            self.consulta,
            veterinario_selecionado
        )
    def exibir_mensagem(self,mensagem, sucesso = True):
        if sucesso: 
            messagebox.showinfo(
                "Mini ERP",
                mensagem, 
                parent = self.root
            )

        else: 
            messagebox.showerror(
                "Mini ERP", 
                mensagem, 
                parent = self.root
            )
    def fechar(self):
        self.root.destroy()
