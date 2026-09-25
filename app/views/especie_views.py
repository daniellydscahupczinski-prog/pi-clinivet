from app.models.especie import Especie
from app.core.idiomas import Idioma

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Especie_View:

    # Paleta de cores dos botões (mesmo padrão usado na Home_View,
    # pra manter o visual consistente em todas as telas do sistema).
    COR_BOTAO = "#C09B7A"
    COR_BOTAO_ATIVO = "#AD8563"
    COR_TEXTO_BOTAO = "#3F2A1D"

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.racas = []
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title(Idioma.t("especie.crud_de_especie"))
        self.root.geometry("800x600")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text=(Idioma.t("especie.janela_titulo")),
            font=("Arial", 16, "bold")
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
            text=(Idioma.t("especie.dados"))
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

        # ID
        self.lbl_id = tk.Label(self.frm_dados, text="ID")
        self.lbl_id.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.txt_id = tk.Entry(self.frm_dados, width=10, state="readonly")
        self.txt_id.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Nome
        self.lbl_nome = tk.Label(self.frm_dados, text="Nome:")
        self.lbl_nome.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.txt_nome = tk.Entry(self.frm_dados, width=40)
        self.txt_nome.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Raça - agora logo abaixo do Nome
        self.lbl_raca = tk.Label(self.frm_dados, text="Raça:")
        self.lbl_raca.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.cmb_raca = ttk.Combobox(
            self.frm_dados,
            width=37,
            state="readonly"
        )
        self.cmb_raca.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Botões
        self.frm_botoes = tk.Frame(
            self.frm_dados,
            border=2,
            relief="groove"
        )
        self.frm_botoes.grid(
            row=3,
            column=0,
            padx=10,
            pady=5,
            columnspan=4,
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
        self.btn_novo.grid(row=0, column=0, padx=5, pady=5)

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
        self.btn_salvar.grid(row=0, column=1, padx=5, pady=5)

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
        self.btn_alterar.grid(row=0, column=2, padx=5, pady=5)

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
        self.btn_excluir.grid(row=0, column=3, padx=5, pady=5)

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
        self.btn_fechar.grid(row=0, column=4, padx=5, pady=5)

        # Tabela de espécies (antes não existia!)
        self.frm_tabela = tk.Frame(self.root)
        self.frm_tabela.grid(
            row=4,
            column=0,
            columnspan=4,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.tbl_especie = ttk.Treeview(self.frm_tabela, show="headings")
        self.scroll_tabela = ttk.Scrollbar(
            self.frm_tabela,
            orient="vertical",
            command=self.tbl_especie.yview
        )
        self.tbl_especie.configure(yscrollcommand=self.scroll_tabela.set)

        self.tbl_especie.pack(side="left", fill="both", expand=True)
        self.scroll_tabela.pack(side="right", fill="y")

    def configurar_treeview(self):
        self.tbl_especie["columns"] = ("id", "nome", "raca")
        self.tbl_especie.column("id", width=40, anchor="center")
        self.tbl_especie.column("nome", width=200)
        self.tbl_especie.column("raca", width=200)
        self.tbl_especie.heading("id", text=(Idioma.t("comum.id")))
        self.tbl_especie.heading("nome", text=(Idioma.t("comum.nome")))
        self.tbl_especie.heading("raca", text=(Idioma.t("menu.raca")))

    def configurar_eventos(self):
        self.btn_novo.config(command=self.controller.new)
        self.btn_salvar.config(command=self.controller.save)
        self.btn_alterar.config(command=self.controller.update)
        self.btn_excluir.config(command=self.controller.delete)
        self.btn_fechar.config(command=self.fechar)
        self.tbl_especie.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_especie
        )

    def carregar_racas(self, racas):
        self.racas = racas
        self.cmb_raca["values"] = [raca.nome for raca in racas]

    def preencher_campos(self, especie):
        self.limpar_campos()
        self.txt_id.config(state="normal")
        self.txt_id.insert(0, str(especie.id))
        self.txt_id.config(state="readonly")
        self.txt_nome.insert(0, especie.nome)

    def limpar_campos(self):
        self.txt_id.config(state="normal")
        self.txt_id.delete(0, tk.END)
        self.txt_id.config(state="readonly")
        self.txt_nome.delete(0, tk.END)
        self.cmb_raca.set("")
        self.txt_nome.focus()

    def limpar_treeview(self):
        for item in self.tbl_especie.get_children():
            self.tbl_especie.delete(item)

    def get_id_selecionado(self):
        item = self.tbl_especie.selection()[0]
        return self.tbl_especie.item(item)["values"][0]

    def get_raca_selecionada(self):
        indice = self.cmb_raca.current()
        if indice < 0:
            raise ValueError("Selecione uma raça.")
        return self.racas[indice]

    def confirmar_exclusao(self):
        return messagebox.askyesno(
            (Idioma.t("comum.confirmacao")),
            (Idioma.t("especie.confirmacao_exclusao")),
            parent=self.root
        )

    def ler_dados_especie(self):
        nome = self.txt_nome.get()
        return nome

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            messagebox.showinfo("mini ERP", mensagem, parent=self.root)
        else:
            messagebox.showerror("Mini ERP", mensagem, parent=self.root)


        self.root.lift()
        self.root.focus_force()

    def exibir_especies(self, especies):
        self.limpar_treeview()
        for especie in especies:
            nome_raca = especie.raca.nome if especie.raca else ""
            self.tbl_especie.insert(
                "",
                tk.END,
                values=(especie.id, especie.nome, nome_raca)
            )

    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.carregar_racas()
        self.controller.get_all()