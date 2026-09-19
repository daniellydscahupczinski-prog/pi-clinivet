from app.models.cliente import Cliente

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Cliente_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title("Crud de Clientes")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = ("Cadastro de cliente"),
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
            text = ("Dados do cliente")
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
            text = "ID:"
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
            text = ("Nome")
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
            text = ("Numero de telefone:")
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
            text = ("Numero do cpf:")
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
            text = (("Novo")),
            width = 15
        )
        self.btn_novo.grid(
            row = 0,
            column = 0,
            padx = 5,
            pady = 5
        )
        self.btn_salvar = tk.Button(
            self.frm_botoes,
            text = (("Salvar")),
            width = 15
        )
        self.btn_salvar.grid(
            row = 0,
            column = 1,
            padx = 5,
            pady = 5
        )
        self.btn_alterar = tk.Button(
            self.frm_botoes,
            text = (("Alterar")),
            width = 15
        )
        self.btn_alterar.grid(
            row = 0,
            column = 2,
            padx = 5,
            pady = 5
        )
        self.btn_excluir = tk.Button(
            self.frm_botoes,
            text = (("Excluir")),
            width = 15
        )
        self.btn_excluir.grid(
            row = 0,
            column = 3,
            padx = 5,
            pady = 5
        )
        self.btn_fechar = tk.Button(
            self.frm_botoes,
            text = (("Fechar")),
            width = 15
        )
        self.btn_fechar.grid(
            row = 0,
            column = 4,
            padx = 5,
            pady = 5
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
            text = "ID"
        )
        self.tbl_cliente.heading(
            "nome",
            text = "Nome"
        )
        self.tbl_cliente.heading(
            "telefone",
            text = "Telefone"
        )
        self.tbl_cliente.heading(
            "cpf",
            text = "CPF"
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
            (("confirmacao")),
            (("Deseja realmente excluir este cliente?")),
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