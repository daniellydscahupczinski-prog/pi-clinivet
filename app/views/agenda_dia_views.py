import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from app.core.idiomas import Idioma
class Agenda_Dia_View:

    # Paleta de cores dos botões (mesmo padrão usado na Home_View,
    # pra manter o visual consistente em todas as telas do sistema).
    COR_BOTAO = "#C09B7A"
    COR_BOTAO_ATIVO = "#AD8563"
    COR_TEXTO_BOTAO = "#3F2A1D"

    def __init__(self, root, dao_agendamento):
        self.root = root
        self.dao_agendamento = dao_agendamento
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()

    def configurar_janela(self):
        self.root.title(Idioma.t("agenda.agenda_dia"))
        self.root.geometry("700x500")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text=(Idioma.t("agenda.agenda_data")),
            font=("Arial", 16, "bold")
        )
        self.lbl_titulo.grid(
            row=0,
            column=0,
            columnspan=3,
            padx=5,
            pady=10
        )

        self.lbl_data = tk.Label(
            self.root,
            text=(Idioma.t("agenda.data_dia"))
        )
        self.lbl_data.grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.txt_data = tk.Entry(
            self.root,
            width=15
        )
        self.txt_data.grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.btn_buscar = tk.Button(
            self.root,
            text=(Idioma.t("agenda.busca")),
            width=15,
            bg=self.COR_BOTAO,
            fg=self.COR_TEXTO_BOTAO,
            activebackground=self.COR_BOTAO_ATIVO,
            activeforeground=self.COR_TEXTO_BOTAO,
            relief="flat",
            cursor="hand2",
            command=self.buscar
        )
        self.btn_buscar.grid(
            row=1,
            column=2,
            padx=5,
            pady=5
        )

        self.tbl_agenda = ttk.Treeview(
            self.root,
            height=15
        )
        self.tbl_agenda.grid(
            row=2,
            column=0,
            columnspan=3,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.btn_concluir = tk.Button(
            self.root,
            text=(Idioma.t("agenda.marcar_concluido")),
            width=20,
            bg=self.COR_BOTAO,
            fg=self.COR_TEXTO_BOTAO,
            activebackground=self.COR_BOTAO_ATIVO,
            activeforeground=self.COR_TEXTO_BOTAO,
            relief="flat",
            cursor="hand2",
            command=self.marcar_concluido
        )
        self.btn_concluir.grid(
            row=3,
            column=0,
            columnspan=3,
            padx=5,
            pady=10
        )

    def configurar_treeview(self):
        self.tbl_agenda["columns"] = (
            "id",
            "servico",
            "horario",
            "status"
        )
        self.tbl_agenda.column(
            "#0",
            width=0,
            stretch=False
        )
        self.tbl_agenda.column(
            "id",
            width=10,
            anchor="center"
        )
        self.tbl_agenda.column(
            "servico",
            width=250
        )
        self.tbl_agenda.column(
            "horario",
            width=100,
            anchor="center"
        )
        self.tbl_agenda.column(
            "status",
            width=150
        )
        self.tbl_agenda.heading(
            "id",
            text=(Idioma.t("comum.id"))
        )
        self.tbl_agenda.heading(
            "servico",
            text=(Idioma.t("agenda.servico"))
        )
        self.tbl_agenda.heading(
            "horario",
            text=(Idioma.t("agenda.horario"))
        )
        self.tbl_agenda.heading(
            "status",
            text=(Idioma.t("agenda.status"))
        )

    def limpar_treeview(self):
        for item in self.tbl_agenda.get_children():
            self.tbl_agenda.delete(item)

    def buscar(self):
        data = self.txt_data.get()

        if not data:
            messagebox.showerror(
                (Idioma.t("agenda.agenda_dia")),
                (Idioma.t("agenda.digite_data")),
                parent=self.root
            )
            return

        agendamentos = self.dao_agendamento.get_por_data(data)

        self.limpar_treeview()

        for agendamento in agendamentos:
            self.tbl_agenda.insert(
                "",
                tk.END,
                values=(
                    agendamento.id,
                    agendamento.servico,
                    agendamento.horario_agendamento,
                    agendamento.status_agendamento
                )
            )

    def marcar_concluido(self):
        selecionado = self.tbl_agenda.selection()

        if not selecionado:
            messagebox.showerror(
                (Idioma.t("agenda.agenda_dia")),
                (Idioma.t("agenda.selecionar_agendamento")),
                parent=self.root
            )
            return

        item = self.tbl_agenda.item(selecionado[0])
        id_agendamento = item["values"][0]

        agendamento = self.dao_agendamento.get_by_id(id_agendamento)

        if agendamento is None:
            messagebox.showerror(
                (Idioma.t("agenda.agenda_dia")),
                (Idioma.t("agenda.nao_encontrado")),
                parent=self.root
            )
            return

        agendamento.status_agendamento = (Idioma.t("agenda.concluido"))

        self.dao_agendamento.update(agendamento)

        messagebox.showinfo(
            (Idioma.t("agenda.agenda_dia")),
            (Idioma.t("agenda.marcado_concluido")),
            parent=self.root
        )

        self.buscar()