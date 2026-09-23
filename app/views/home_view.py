import os
import tkinter as tk

from PIL import Image, ImageTk


class Home_View:

    # Caminho do arquivo da marca d'água (logo CliniVet).
    # Calculado a partir da localização deste arquivo
    # (app/views/home_view.py), então funciona não importa
    # de onde você execute o main.py.
    # app/views/home_view.py -> sobe 1 nível -> app/ -> assets/watermark.png
    _DIR_APP = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
    CAMINHO_MARCA_DAGUA = os.path.join(
        _DIR_APP, "assets", "watermark.png"
    )

    # Tamanho (em pixels) que a marca d'água terá na tela.
    TAMANHO_MARCA_DAGUA = (800, 700)

    def __init__(self, root, controller):

        self.root = root
        self.controller = controller

        # Precisa manter referência da imagem, senão o
        # garbage collector do Python apaga e ela some da tela.
        self._watermark_photo = None

        self.configurar_janela()
        self.criar_componentes()

    def configurar_janela(self):

        self.root.title("Sistema Corporativo ERP")

        self.root.geometry("1000x700")

        self.root.configure(
            bg="#FFF9F2"
        )

    def criar_componentes(self):

        # =====================================
        # TÍTULO
        # =====================================

        self.lbl_titulo = tk.Label(
            self.root,
            text="BEM VINDO(A)\nÀ CLINIVET!",
            font=("Georgia", 26, "bold"),
            bg="#FFF9F2",
            fg="#5A3E2B",
            justify="left"
        )

        self.lbl_titulo.pack(
            anchor="w",
            padx=80,
            pady=(60, 5)
        )


        # =====================================
        # SUBTÍTULO
        # =====================================

        self.lbl_subtitulo = tk.Label(
            self.root,
            text="Como podemos lhe ajudar hoje?",
            font=("Georgia", 14),
            bg="#FFF9F2",
            fg="#5A3E2B"
        )

        self.lbl_subtitulo.pack(
            anchor="w",
            padx=100,
            pady=(0, 30)
        )


        # =====================================
        # ÁREA DOS BOTÕES (com a marca d'água atrás)
        # =====================================
        # Usamos um Frame + .place() (em vez de .grid()) porque
        # .place() permite sobrepor widgets: a marca d'água fica
        # "embaixo" e os botões ficam "em cima", na mesma área.

        self.frm_botoes = tk.Frame(
            self.root,
            bg="#FFF9F2"
        )

        self.frm_botoes.pack(
            fill="both",
            expand=True
        )

        # -------------------------------------
        # MARCA D'ÁGUA (fica atrás dos botões)
        # -------------------------------------

        self._criar_marca_dagua()

        # -------------------------------------
        # BOTÃO CADASTROS
        # -------------------------------------

        self.btn_cadastros = tk.Button(
            self.frm_botoes,
            text="Cadastros\nBásicos",
            font=("Georgia", 16, "bold"),
            bg="#C09B7A",
            fg="#3F2A1D",
            width=15,
            height=5,
            relief="flat",
            cursor="hand2",
            command=self.controller.abrir_cadastros
        )

        self.btn_cadastros.place(
            relx=0.25,
            rely=0.32,
            anchor="center"
        )

        # -------------------------------------
        # BOTÃO MENUS
        # -------------------------------------

        self.btn_menus = tk.Button(
            self.frm_botoes,
            text="Menus",
            font=("Georgia", 16, "bold"),
            bg="#C09B7A",
            fg="#3F2A1D",
            width=15,
            height=5,
            relief="flat",
            cursor="hand2",
            command=self.controller.abrir_menus
        )

        self.btn_menus.place(
            relx=0.75,
            rely=0.32,
            anchor="center"
        )

        # -------------------------------------
        # BOTÃO ACESSOS
        # -------------------------------------

        self.btn_acessos = tk.Button(
            self.frm_botoes,
            text="Acessos",
            font=("Georgia", 16, "bold"),
            bg="#C09B7A",
            fg="#3F2A1D",
            width=15,
            height=5,
            relief="flat",
            cursor="hand2",
            command=self.controller.abrir_acessos
        )

        self.btn_acessos.place(
            relx=0.25,
            rely=0.68,
            anchor="center"
        )

        # -------------------------------------
        # BOTÃO SAIR
        # -------------------------------------

        self.btn_sair = tk.Button(
            self.frm_botoes,
            text="Sair",
            font=("Georgia", 16, "bold"),
            bg="#BDA58F",
            fg="#3F2A1D",
            width=15,
            height=5,
            relief="flat",
            cursor="hand2",
            command=self.controller.sair
        )

        self.btn_sair.place(
            relx=0.75,
            rely=0.68,
            anchor="center"
        )

    def _criar_marca_dagua(self):
        """
        Carrega o arquivo de marca d'água (logo CliniVet) e a
        posiciona centralizada, atrás dos botões.

        Se o arquivo não existir ainda, a tela funciona normalmente
        (só sem a marca d'água) e um aviso é impresso no console.
        """

        if not os.path.exists(self.CAMINHO_MARCA_DAGUA):
            print(
                f"[Aviso] Marca d'água não encontrada em: "
                f"{self.CAMINHO_MARCA_DAGUA}"
            )
            return

        imagem = Image.open(self.CAMINHO_MARCA_DAGUA).convert("RGBA")
        imagem = imagem.resize(
            self.TAMANHO_MARCA_DAGUA,
            Image.LANCZOS
        )

        self._watermark_photo = ImageTk.PhotoImage(imagem)

        self.lbl_marca_dagua = tk.Label(
            self.frm_botoes,
            image=self._watermark_photo,
            bg="#FFF9F2",
            bd=0,
            highlightthickness=0
        )

        self.lbl_marca_dagua.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )