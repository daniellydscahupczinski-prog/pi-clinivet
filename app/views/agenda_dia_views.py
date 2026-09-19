import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Agenda_Dia_View:
    def __init__(self, root, dao_agendamento):
        self.root = root
        self.dao_agendamento = dao_agendamento
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()

    def configurar_janela(self):
        self.root.title("Agenda do dia")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text="Agenda por data",
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
            text="Data (AAAA-MM-DD):"
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
            text="Buscar",
            width=15,
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
            text="Marcar concluído",
            width=20,
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
            text="ID"
        )
        self.tbl_agenda.heading(
            "servico",
            text="Serviço"
        )
        self.tbl_agenda.heading(
            "horario",
            text="Horário"
        )
        self.tbl_agenda.heading(
            "status",
            text="Status"
        )

    def limpar_treeview(self):
        for item in self.tbl_agenda.get_children():
            self.tbl_agenda.delete(item)

    def buscar(self):
        data = self.txt_data.get()

        if not data:
            messagebox.showerror(
                "Agenda do dia",
                "Digite uma data",
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
                "Agenda do dia",
                "Selecione um agendamento na lista",
                parent=self.root
            )
            return

        item = self.tbl_agenda.item(selecionado[0])
        id_agendamento = item["values"][0]

        agendamento = self.dao_agendamento.get_by_id(id_agendamento)

        if agendamento is None:
            messagebox.showerror(
                "Agenda do dia",
                "Agendamento não encontrado",
                parent=self.root
            )
            return

        agendamento.status_agendamento = "Concluido"

        self.dao_agendamento.update(agendamento)

        messagebox.showinfo(
            "Agenda do dia",
            "Agendamento marcado como concluído!",
            parent=self.root
        )

        self.buscar()