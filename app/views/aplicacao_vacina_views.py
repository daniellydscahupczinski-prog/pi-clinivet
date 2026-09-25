import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from app.core.idiomas import Idioma

class Aplicacao_Vacina_View:

    # Paleta de cores dos botões (mesmo padrão usado na Home_View,
    # pra manter o visual consistente em todas as telas do sistema).
    COR_BOTAO = "#C09B7A"
    COR_BOTAO_ATIVO = "#AD8563"
    COR_TEXTO_BOTAO = "#3F2A1D"

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self._aplicacoes_vacina = []

        self.configurar__janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar__janela(self):
        self.root.title(Idioma.t("aplicacao_vacina.janela_titulo"))
        self.root.geometry("900x600")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text=(Idioma.t("aplicacao_vacina.titulo")),
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
            text=(Idioma.t("aplicacao_vacina.dadso_frame"))
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

        self.lbl_tipo_servico = tk.Label(
            self.frm_dados,
            text=(Idioma.t("aplicacao_vacina.tipo_servico"))
        )
        self.lbl_tipo_servico.grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.txt_tipo_servico = tk.Entry(
            self.frm_dados,
            width=40
        )
        self.txt_tipo_servico.grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.lbl_data_vacina = tk.Label(
            self.frm_dados,
            text=(Idioma.t("aplicacao_vacina.data_vacina"))
        )
        self.lbl_data_vacina.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.txt_data_vacina = tk.Entry(
            self.frm_dados,
            width=20
        )
        self.txt_data_vacina.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.lbl_horario_vacina = tk.Label(
            self.frm_dados,
            text=(Idioma.t("aplicacao_vacina.horario_vacina"))
        )
        self.lbl_horario_vacina.grid(
            row=3,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.txt_horario_vacina = tk.Entry(
            self.frm_dados,
            width=20
        )
        self.txt_horario_vacina.grid(
            row=3,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.lbl_status_vacina = tk.Label(
            self.frm_dados,
            text=(Idioma.t("aplicacao_vacina.status_vacina"))
        )
        self.lbl_status_vacina.grid(
            row=4,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.txt_status_vacina = tk.Entry(
            self.frm_dados,
            width=20
        )
        self.txt_status_vacina.grid(
            row=4,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.lbl_animal_id = tk.Label(
            self.frm_dados,
            text=(Idioma.t("aplicacao_vacina.animal_id"))
        )
        self.lbl_animal_id.grid(
            row=5,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.txt_animal_id = tk.Entry(
            self.frm_dados,
            width=20
        )
        self.txt_animal_id.grid(
            row=5,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.lbl_vacina_id = tk.Label(
            self.frm_dados,
            text=(Idioma.t("aplicacao_vacina.vacina_id"))
        )
        self.lbl_vacina_id.grid(
            row=6,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.txt_vacina_id = tk.Entry(
            self.frm_dados,
            width=20
        )
        self.txt_vacina_id.grid(
            row=6,
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
            row=7,
            column=0,
            padx=10,
            pady=5,
            columnspan=4
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

        self.tbl_aplicacoes_vacina = ttk.Treeview(
            self.root,
            height=10
        )
        self.tbl_aplicacoes_vacina.grid(
            row=8,
            column=0,
            columnspan=4,
            padx=10,
            pady=10,
            sticky="nsew"
        )

    def configurar_treeview(self):
        self.tbl_aplicacoes_vacina["columns"] = (
            "id",
            "tipo_servico",
            "data_vacina",
            "horario_vacina",
            "status_vacina",
            "animal_id",
            "vacina_id"
        )

        self.tbl_aplicacoes_vacina.column(
            "#0",
            width=0,
            stretch=False
        )

        self.tbl_aplicacoes_vacina.column(
            "id",
            width=50,
            anchor="center"
        )

        self.tbl_aplicacoes_vacina.column(
            "tipo_servico",
            width=100
        )

        self.tbl_aplicacoes_vacina.column(
            "data_vacina",
            width=100
        )

        self.tbl_aplicacoes_vacina.column(
            "horario_vacina",
            width=100
        )

        self.tbl_aplicacoes_vacina.column(
            "status_vacina",
            width=100
        )

        self.tbl_aplicacoes_vacina.column(
            "animal_id",
            width=80
        )

        self.tbl_aplicacoes_vacina.column(
            "vacina_id",
            width=80
        )

        self.tbl_aplicacoes_vacina.heading(
            "id",
            text=(Idioma.t("comum.id"))
        )

        self.tbl_aplicacoes_vacina.heading(
            "tipo_servico",
            text=(Idioma.t("aplicacao_vacina.tipo_servico"))
        )

        self.tbl_aplicacoes_vacina.heading(
            "data_vacina",
            text=(Idioma.t("aplicacao_vacina.data_vacina"))
        )

        self.tbl_aplicacoes_vacina.heading(
            "horario_vacina",
            text=(Idioma.t("aplicacao_vacina.horario_vacina"))
        )
        self.tbl_aplicacoes_vacina.heading(
            "status_vacina",
            text=(Idioma.t("aplicacao_vacina.status_vacina"))
        )

        self.tbl_aplicacoes_vacina.heading(
            "animal_id",
            text=(Idioma.t("aplicacao_vacina.animal_id"))
        )

        self.tbl_aplicacoes_vacina.heading(
            "vacina_id",
            text=(Idioma.t("aplicacao_vacina.vacina_id"))
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

        self.tbl_aplicacoes_vacina.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_aplicacoes_vacina
        )

    def preencher_campos(self, aplicacao_vacina):
        self.limpar_campos()

        self.txt_id.config(state="normal")
        self.txt_id.insert(
            0,
            str(aplicacao_vacina.id)
        )
        self.txt_id.config(state="readonly")

        self.txt_tipo_servico.insert(
            0,
            aplicacao_vacina.tipo_servico
        )

        self.txt_data_vacina.insert(
            0,
            aplicacao_vacina.data_vacina
        )

        self.txt_horario_vacina.insert(
            0,
            aplicacao_vacina.horario_vacina
        )

        self.txt_status_vacina.insert(
            0,
            aplicacao_vacina.status_vacina
        )

        self.txt_animal_id.insert(
            0,
            aplicacao_vacina.animal_id
        )

        self.txt_vacina_id.insert(
            0,
            aplicacao_vacina.vacina_id
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

        self.txt_tipo_servico.delete(
            0,
            tk.END
        )

        self.txt_data_vacina.delete(
            0,
            tk.END
        )

        self.txt_horario_vacina.delete(
            0,
            tk.END
        )

        self.txt_status_vacina.delete(
            0,
            tk.END
        )

        self.txt_animal_id.delete(
            0,
            tk.END
        )

        self.txt_vacina_id.delete(
            0,
            tk.END
        )

        self.txt_tipo_servico.focus()

    def limpar_treeview(self):
        for item in self.tbl_aplicacoes_vacina.get_children():
            self.tbl_aplicacoes_vacina.delete(item)

    def get_id_selecionado(self):
        item = self.tbl_aplicacoes_vacina.selection()[0]
        return self.tbl_aplicacoes_vacina.item(item)["values"][0]

    def confirmar_exclusao(self):
        return messagebox.askyesno(
            (Idioma.t("comum.confirmacao")),
            (Idioma.t("aplicacao_vacina.confirmacao_exclusao")),
            parent=self.root
        )

    def ler_dados_aplicacao_vacina(self):
        tipo_servico = self.txt_tipo_servico.get()
        data_vacina = self.txt_data_vacina.get()
        horario_vacina = self.txt_horario_vacina.get()
        status_vacina = self.txt_status_vacina.get()
        animal_id = self.txt_animal_id.get()
        vacina_id = self.txt_vacina_id.get()

        return (
            tipo_servico,
            data_vacina,
            horario_vacina,
            status_vacina,
            animal_id,
            vacina_id
        )

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

    def exibir_aplicacoes_vacina(self, aplicacoes_vacina):
        self.limpar_treeview()

        for aplicacao_vacina in aplicacoes_vacina:
            self.tbl_aplicacoes_vacina.insert(
                "",
                tk.END,
                values=(
                    aplicacao_vacina.id,
                    aplicacao_vacina.tipo_servico,
                    aplicacao_vacina.data_vacina,
                    aplicacao_vacina.horario_vacina,
                    aplicacao_vacina.status_vacina,
                    aplicacao_vacina.animal_id,
                    aplicacao_vacina.vacina_id
                )
            )

    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.get_all()