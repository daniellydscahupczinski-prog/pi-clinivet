from app.models.animal import Animal
from app.core.data_utils import Data_Utils
from app.core.idiomas import Idioma

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Animal_View:

    # Paleta de cores dos botões (mesmo padrão usado na Home_View,
    # pra manter o visual consistente em todas as telas do sistema).
    COR_BOTAO = "#C09B7A"
    COR_BOTAO_ATIVO = "#AD8563"
    COR_TEXTO_BOTAO = "#3F2A1D"

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self._animais = []
        self.configurar__janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar__janela(self):
        self.root.title(Idioma.t("animal.janela_titulo"))
        self.root.geometry("900x600")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text=(Idioma.t("animal.titulo")),
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
            text=(Idioma.t("animal.dados_frame"))
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
            text=(Idioma.t("comum.id"))
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
            text=(Idioma.t("comum.nome"))
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
        self.lbl_data_nascimento = tk.Label(
            self.frm_dados,
            text=(Idioma.t("animal.data_nascimento"))
        )
        self.lbl_data_nascimento.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.txt_data_nascimento = tk.Entry(
            self.frm_dados,
            width=20
        )
        self.txt_data_nascimento.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.lbl_sexo = tk.Label(
            self.frm_dados,
            text=(Idioma.t("animal.sexo"))
        )
        self.lbl_sexo.grid(
            row=3,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.txt_sexo = tk.Entry(
            self.frm_dados,
            width=20
        )
        self.txt_sexo.grid(
            row=3,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.lbl_peso = tk.Label(
            self.frm_dados,
            text=(Idioma.t("animal.peso"))
        )
        self.lbl_peso.grid(
            row=4,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.txt_peso = tk.Entry(
            self.frm_dados,
            width=20
        )
        self.txt_peso.grid(
            row=4,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.lbl_cliente_id = tk.Label(
            self.frm_dados,
            text=(Idioma.t("animal.cliente_id"))
        )
        self.lbl_cliente_id.grid(
            row=5,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.txt_cliente_id = tk.Entry(
            self.frm_dados,
            width=20
        )
        self.txt_cliente_id.grid(
            row=5,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.lbl_especie_id = tk.Label(
            self.frm_dados,
            text=(Idioma.t("animal.especie_id"))
        )
        self.lbl_especie_id.grid(
            row=6,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.txt_especie_id = tk.Entry(
            self.frm_dados,
            width=20
        )
        self.txt_especie_id.grid(
            row=6,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.lbl_raca_id = tk.Label(
            self.frm_dados,
            text=(Idioma.t("animal.raca_id"))
        )
        self.lbl_raca_id.grid(
            row=7,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )
        self.txt_raca_id = tk.Entry(
            self.frm_dados,
            width=20
        )
        self.txt_raca_id.grid(
            row=7,
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
            row=8,
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
        self.tbl_animais = ttk.Treeview(
            self.root,
            height=10
        )
        self.tbl_animais.grid(
            row=9,
            column=0,
            columnspan=4,
            padx=10,
            pady=10,
            sticky="nsew"
        )

    def configurar_treeview(self):
        self.tbl_animais["columns"] = (
            "id",
            "nome",
            "data_nascimento",
            "sexo",
            "peso",
            "cliente_id",
            "especie_id",
            "raca_id"
        )
        self.tbl_animais.column(
            "#0",
            width=0,
            stretch=False
        )
        self.tbl_animais.column(
            "id",
            width=5,
            anchor="center"
        )
        self.tbl_animais.column(
            "nome",
            width=50
        )
        self.tbl_animais.column(
            "data_nascimento",
            width=20
        )
        self.tbl_animais.column(
            "sexo",
            width=30
        )
        self.tbl_animais.column(
            "peso",
            width=5
        )
        self.tbl_animais.column(
            "cliente_id",
            width=5
        )
        self.tbl_animais.column(
            "especie_id",
            width=5
        )
        self.tbl_animais.column(
            "raca_id",
            width=5
        )
        self.tbl_animais.heading(
            "id",
            text=(Idioma.t("comum.id"))
        )
        self.tbl_animais.heading(
            "nome",
            text=(Idioma.t("comum.nome"))
        )
        self.tbl_animais.heading(
            "data_nascimento",
            text=(Idioma.t("animal.data_nascimento"))
        )
        self.tbl_animais.heading(
            "sexo",
            text=(Idioma.t("animal.sexo"))
        )
        self.tbl_animais.heading(
            "peso",
            text=(Idioma.t("animal.peso"))
        )
        self.tbl_animais.heading(
            "cliente_id",
            text=(Idioma.t("animal.cliente_id"))
        )
        self.tbl_animais.heading(
            "especie_id",
            text=(Idioma.t("animal.especie_id"))
        )
        self.tbl_animais.heading(
            "raca_id",
            text=(Idioma.t("animal.raca_id"))
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
        self.tbl_animais.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_animal
        )

    def preencher_campos(self, animal):
        self.limpar_campos()
        self.txt_id.config(state="normal")
        self.txt_id.insert(
            0,
            str(animal.id)
        )
        self.txt_id.config(state="readonly")
        self.txt_nome.insert(
            0,
            animal.nome
        )
        self.txt_data_nascimento.insert(
            0,
            animal.data_nascimento
        )
        self.txt_sexo.insert(
            0,
            animal.sexo
        )
        self.txt_peso.insert(
            0,
            animal.peso
        )
        self.txt_cliente_id.insert(
            0,
            animal.cliente_id
        )
        self.txt_especie_id.insert(
            0,
            animal.especie_id
        )
        self.txt_raca_id.insert(
            0,
            animal.raca_id
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
        self.txt_data_nascimento.delete(
            0,
            tk.END
        )
        self.txt_sexo.delete(
            0,
            tk.END
        )
        self.txt_peso.delete(
            0,
            tk.END
        )
        self.txt_cliente_id.delete(
            0,
            tk.END
        )
        self.txt_especie_id.delete(
            0,
            tk.END
        )
        self.txt_raca_id.delete(
            0,
            tk.END
        )
        self.txt_nome.focus()

    def limpar_treeview(self):
        for item in self.tbl_animais.get_children():
            self.tbl_animais.delete(item)

    def get_id_selecionado(self):
        item = self.tbl_animais.selection()[0]
        return self.tbl_animais.item(item)["values"][0]

    def confirmar_exclusao(self):
        return messagebox.askyesno(
            (Idioma.t("comum.confirmacao")),
            (Idioma.t("animal.confirmacao_exclusao")),
            parent=self.root
        )

    def ler_dados_animal(self):
        nome = self.txt_nome.get()
        data_nascimento = self.txt_data_nascimento.get()
        sexo = self.txt_sexo.get()
        peso = self.txt_peso.get()
        cliente_id = self.txt_cliente_id.get()
        especie_id = self.txt_especie_id.get()
        raca_id = self.txt_raca_id.get()
        return nome, data_nascimento, sexo, peso, cliente_id, especie_id, raca_id

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

    def exibir_animal(self, animais):
        self.limpar_treeview()
        for animal in animais:
            self.tbl_animais.insert(
                "",
                tk.END,
                values=(
                    animal.id,
                    animal.nome,
                    animal.data_nascimento,
                    animal.sexo,
                    animal.peso,
                    animal.cliente_id,
                    animal.especie_id,
                    animal.raca_id,
                )
            )

    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.carregar_clientes()
        self.controller.carregar_especie()
        self.controller.carregar_raca()
        self.controller.get_all()