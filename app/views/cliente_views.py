from app.models.cliente import Cliente
from app.core.idiomas import Idioma

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Cliente_View:

    # Paleta de cores dos botões (mesmo padrão usado na Home_View,
    # pra manter o visual consistente em todas as telas do sistema).
    COR_BOTAO = "#C09B7A"
    COR_BOTAO_ATIVO = "#AD8563"
    COR_TEXTO_BOTAO = "#3F2A1D"

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title(Idioma.t("cliente.janela_titulo"))
        self.root.geometry("800x600")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = (Idioma.t("cliente.titulo")),
            font = ("arial", 16, "bold")
        )
        self.lbl_titulo.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            padx = 5,
            pady = 5
        )
        self.frm_dados = tk.LabelFrame(
            self.root,
            text = (Idioma.t("cliente.dados_frame"))
        )
        self.frm_dados.grid(
            row = 1,
            column = 0,
            columnspan=2,
            padx = 10,
            pady = 5,
            sticky = "ew"
        )
        self.frm_dados.grid_columnconfigure(0, weight=0)
        self.frm_dados.grid_columnconfigure(1, weight=1)
        self.lbl_id = tk.Label(
            self.frm_dados,
            text = (Idioma.t( "comum.id"))
        )
        self.lbl_id.grid(
            row = 0,
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
            column= 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_nome = tk.Label(
            self.frm_dados,
            text = (Idioma.t("comum.nome"))
        )
        self.lbl_nome.grid(
            row = 1,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_nome = tk.Entry(
            self.frm_dados,
            width = 40
        )
        self.txt_nome.grid(
            row = 1,
            column = 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_telefone = tk.Label(
            self.frm_dados,
            text = (Idioma.t("cliente.telefone"))
        )
        self.lbl_telefone.grid(
            row = 2,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"            
        )
        self.txt_telefone = tk.Entry(
            self.frm_dados,
            width = 40
        )
        self.txt_telefone.grid(
            row = 2,
            column = 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_cpf = tk.Label(
            self.frm_dados,
            text = (Idioma.t("cliente.cpf"))
        )
        self.lbl_cpf.grid(
            row = 3,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_cpf = tk.Entry(
            self.frm_dados,
            width = 40
        )
        self.txt_cpf.grid(
            row = 3,
            column = 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.frm_botoes = tk.Frame(
            self.frm_dados,
            border = 2,
            relief = "groove"
        )
        self.frm_botoes.grid(
            row = 4,
            column = 0,
            padx = 10,
            pady = 5,
            columnspan = 2,
        )
        self.btn_novo = tk.Button(
            self.frm_botoes,
            text=(Idioma.t("comum.novo")),
            width=15,
            bg=self.COR_BOTAO,
            fg=self.COR_TEXTO_BOTAO,
            activebackground=self.COR_BOTAO_ATIVO,
            activeforeground=self.COR_TEXTO_BOTAO,
            relief="flat",
            cursor="hand2"
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
            width=15,
            bg=self.COR_BOTAO,
            fg=self.COR_TEXTO_BOTAO,
            activebackground=self.COR_BOTAO_ATIVO,
            activeforeground=self.COR_TEXTO_BOTAO,
            relief="flat",
            cursor="hand2"
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
            width=15,
            bg=self.COR_BOTAO,
            fg=self.COR_TEXTO_BOTAO,
            activebackground=self.COR_BOTAO_ATIVO,
            activeforeground=self.COR_TEXTO_BOTAO,
            relief="flat",
            cursor="hand2"
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
            width=15,
            bg=self.COR_BOTAO,
            fg=self.COR_TEXTO_BOTAO,
            activebackground=self.COR_BOTAO_ATIVO,
            activeforeground=self.COR_TEXTO_BOTAO,
            relief="flat",
            cursor="hand2"
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
            width=15,
            bg=self.COR_BOTAO,
            fg=self.COR_TEXTO_BOTAO,
            activebackground=self.COR_BOTAO_ATIVO,
            activeforeground=self.COR_TEXTO_BOTAO,
            relief="flat",
            cursor="hand2"
        )
        self.btn_fechar.grid(
            row=0,
            column=4,
            padx=5,
            pady=5
        )
        self.tbl_cliente = ttk.Treeview(
            self.root,
            height = 12
        )
        self.tbl_cliente.grid(
            row = 5,
            column = 0,
            columnspan = 2,
            padx = 10,
            pady = 10,
            sticky = "nsew"
        )
    def configurar_treeview(self):
        self.tbl_cliente["columns"] = (
            "id",
            "nome",
            "telefone",
            "cpf"
        )
        self.tbl_cliente.column(
            "#0",
            width = 0,
            stretch = False
        )
        self.tbl_cliente.column(
            "id",
            width = 10,
            anchor = "center"
        )
        self.tbl_cliente.column(
            "nome",
            width = 50
        )
        self.tbl_cliente.column(
            "telefone",
            width = 40
        )
        self.tbl_cliente.column(
            "cpf",
            width = 40
        )
        self.tbl_cliente.heading(
            "id",
            text = (Idioma.t("comum.id"))
        )
        self.tbl_cliente.heading(
            "nome",
            text = (Idioma.t("comum.nome"))
        )
        self.tbl_cliente.heading(
            "telefone",
            text = (Idioma.t("cliente.telefone"))
        )
        self.tbl_cliente.heading(
            "cpf",
            text = (Idioma.t("cliente.cpf"))
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
        self.tbl_cliente.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_cliente

        )

    def preencher_campos(self, cliente):

        self.limpar_campos()
        self.txt_id.config(state = "normal")
        self.txt_id.insert(
            0,
            str(cliente.id)
        )
        self.txt_id.config(state = "readonly")

        self.txt_nome.insert(
            0,
            cliente.nome
        )

        self.txt_telefone.insert(
            0,
            cliente.telefone
        )

        self.txt_cpf.insert(
            0,
            cliente.cpf
        )

    def limpar_campos(self):
        self.txt_id.config(state = "normal")
        self.txt_id.delete(0, tk.END)
        self.txt_id.config(state = "readonly")

        self.txt_nome.delete(0, tk.END)
        self.txt_telefone.delete(0, tk.END)
        self.txt_cpf.delete(0, tk.END)

        self.txt_nome.focus()

    def limpar_treeview(self):
        for item in self.tbl_cliente.get_children():
            self.tbl_cliente.delete(item)

    def get_id_selecionado(self):

        item = self.tbl_cliente.selection()[0]

        return self.tbl_cliente.item(item)["values"][0]
    
    def confirmar_exclusao(self):

        return messagebox.askyesno(
            (Idioma.t("comum.confirmacao")),
            (Idioma.t("cliente.confirmacao_exclusao")),
            parent=self.root
        )
    
    def ler_dados_cliente(self):
        nome = self.txt_nome.get()
        telefone = self.txt_telefone.get()
        cpf = self.txt_cpf.get()
        return nome, telefone, cpf
    
    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            messagebox.showinfo(
                "Mini ERP",
                mensagem,
                parent=self.root
            )
        else:
            messagebox.showerror(
                "Mini ERP",
                mensagem,
                parent=self.root
            )

    def exibir_cliente(self, cliente):

        self.limpar_treeview()

        for cliente in cliente:

            self.tbl_cliente.insert(
                "",
                tk.END,
                values=(
                    cliente.id,
                    cliente.nome,
                    cliente.telefone,
                    cliente.cpf
                )
            )
    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.get_all()