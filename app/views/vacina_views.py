import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Vacina_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self._vacinas = []
        self.configurar__janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar__janela(self):
        self.root.title("CRUD de Vacinas")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text="Criação de vacina",
            font=("Arial", 16, "bold"),
        )
        self.lbl_titulo.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=5,
            pady=5
        )
        self.frm_dados = tk.LabelFrame(
            self.root,
            text="Dados da Vacina"
        )
        self.frm_dados.grid(
            row=1,
            column=0,
            columnspan=4,
            padx=10,
            pady=5,
            sticky="ew"
        )
        self.frm_dados.grid_columnconfigure(0, weight=0)
        self.frm_dados.grid_columnconfigure(1, weight=1)
        self.frm_dados.grid_columnconfigure(2, weight=0)
        self.lbl_id = tk.Label(
            self.frm_dados,
            text="ID:"
        )
        self.lbl_id.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.txt_id = tk.Entry(
            self.frm_dados,
            width=10,
            state="readonly"
        )
        self.txt_id.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.lbl_nome = tk.Label(
            self.frm_dados,
            text="Nome:"
        )
        self.lbl_nome.grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.txt_nome = tk.Entry(
            self.frm_dados,
            width=40
        )
        self.txt_nome.grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.lbl_descricao = tk.Label(
            self.frm_dados,
            text="Descricao"
        )
        self.lbl_descricao.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.txt_descricao = tk.Entry(
            self.frm_dados,
            width=20
        )
        self.txt_descricao.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.frm_botoes = tk.Frame(
            self.frm_dados,
            border=2,
            relief="groove"
        )
        self.frm_botoes.grid(
            row=4,
            column=0,
            padx=10,
            pady=5,
            columnspan=4,
        )
        self.btn_novo = tk.Button(
            self.frm_botoes,
            text="Novo",
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
            text="Salvar",
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
            text="Alterar",
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
            text="Excluir",
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
            text="Fechar",
            width=15
        )
        self.btn_fechar.grid(
            row=0,
            column=4,
            padx=5,
            pady=5
        )
        self.tbl_vacinas = ttk.Treeview(
            self.root,
            height=10
        )
        self.tbl_vacinas.grid(
            row=5,
            column=0,
            columnspan=4,
            padx=10,
            pady=10,
            sticky="nsew"
        )

    def configurar_treeview(self):
        self.tbl_vacinas["columns"] = (
            "id",
            "nome",
            "descricao"
        )
        self.tbl_vacinas.column(
            "#0",
            width=0,
            stretch=False
        )
        self.tbl_vacinas.column(
            "id",
            width=50,
            anchor="center"
        )
        self.tbl_vacinas.column(
            "nome",
            width=300
        )
        self.tbl_vacinas.column(
            "descricao",
            width=400
        )
        self.tbl_vacinas.heading(
            "id",
            text="ID"
        )
        self.tbl_vacinas.heading(
            "nome",
            text="NOME"
        )
        self.tbl_vacinas.heading(
            "descricao",
            text="DESCRIÇÃO"
        )

    def configurar_eventos(self):
        self.btn_novo.config(
            command=self.controller.new
        )
        self.btn_salvar.config(
            command=self.controller.save
        )
        self.btn_alterar.config(
            command=self.controller.update
        )
        self.btn_excluir.config(
            command=self.controller.delete
        )
        self.btn_fechar.config(
            command=self.fechar
        )
        self.tbl_vacinas.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_vacina
        )

    def preencher_campos(self, vacina):
        self.limpar_campos()
        self.txt_id.config(state="normal")
        self.txt_id.insert(
            0,
            str(vacina.id)
        )
        self.txt_id.config(state="readonly")
        self.txt_nome.insert(
            0,
            vacina.nome
        )
        self.txt_descricao.insert(
            0,
            vacina.descricao
        )

    def limpar_campos(self):
        self.txt_id.config(state="normal")
        self.txt_id.delete(
            0,
            tk.END
        )
        self.txt_id.config(
            state="readonly"
        )
        self.txt_nome.delete(
            0,
            tk.END
        )
        self.txt_descricao.delete(
            0,
            tk.END
        )
        self.txt_nome.focus()

    def limpar_treeview(self):
        for item in self.tbl_vacinas.get_children():
            self.tbl_vacinas.delete(item)

    def get_id_selecionado(self):
        item = self.tbl_vacinas.selection()[0]
        return self.tbl_vacinas.item(item)["values"][0]

    def confirmar_exclusao(self):
        return messagebox.askyesno(
            "Confirmação",
            "Deseja realmente excluir esta vacina?",
            parent=self.root
        )

    def ler_dados_vacina(self):
        nome = self.txt_nome.get()
        descricao = self.txt_descricao.get()
        return nome, descricao

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

    def exibir_vacinas(self, vacinas):
        self.limpar_treeview()
        for vacina in vacinas:
            self.tbl_vacinas.insert(
                "",
                tk.END,
                values=(
                    vacina.id,
                    vacina.nome,
                    vacina.descricao,
                )
            )

    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.get_all()