import os
import datetime
import tkinter as tk

from PIL import Image, ImageDraw, ImageTk
from app.core.idiomas import Idioma


# Nomes dos meses em português, usados no cartão "Hoje é: ...".
# Evita depender de locale do sistema operacional (que costuma dar
# problema em máquinas Windows sem o locale pt_BR instalado).
_MESES_PT = {
    1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
    5: "maio", 6: "junho", 7: "julho", 8: "agosto",
    9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro",
}


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

    # Paleta de cores usada em toda a tela.
    COR_FUNDO = "#FFF9F2"
    COR_TEXTO_ESCURO = "#5A3E2B"
    COR_TEXTO_BOTAO = "#3F2A1D"
    COR_BOTAO = "#C09B7A"
    COR_BOTAO_SAIR = "#BDA58F"
    COR_CARTAO = "#F3E6D8"

    def __init__(self, root, controller):

        self.root = root
        self.controller = controller

        # Precisa manter referência das imagens, senão o
        # garbage collector do Python apaga e elas somem da tela.
        self._watermark_photo = None
        self._icones = {}

        self.configurar_janela()
        self.criar_componentes()

    def configurar_janela(self):

        self.root.title(Idioma.t("home_view.janela"))

        self.root.geometry("1000x700")

        self.root.configure(
            bg=self.COR_FUNDO
        )

    # ==========================================================
    # TRADUÇÃO COM FALLBACK
    # ==========================================================
    # Algumas chaves novas (rodapé, "Hoje é:") podem não existir
    # ainda no arquivo de idiomas. Esse helper tenta traduzir e,
    # se a chave não existir, usa o texto padrão em português.
    def _t(self, chave, padrao):
        try:
            texto = Idioma.t(chave)
        except Exception:
            return padrao

        if not texto or texto == chave:
            return padrao

        return texto

    # ==========================================================
    # ÍCONES (desenhados em código, sem depender de arquivos)
    # ==========================================================

    def _criar_icone(self, tipo, tamanho=30, cor="#3F2A1D"):
        """
        Desenha um ícone simples em memória (com PIL) e devolve um
        ImageTk.PhotoImage pronto para usar em Label/Button.
        'tipo' pode ser: 'cadastros', 'menus', 'acessos', 'sair',
        'calendario' ou 'pata'.
        """

        escala = 4  # desenha maior e reduz depois, fica mais suave
        s = tamanho * escala

        img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        margem = s * 0.12
        largura_linha = max(2, int(s * 0.06))

        if tipo == "cadastros":
            # Prancheta com uma pessoa: retângulo + "clipe" no topo + círculo
            d.rounded_rectangle(
                [margem, margem * 1.6, s - margem, s - margem],
                radius=s * 0.08, outline=cor, width=largura_linha
            )
            d.rounded_rectangle(
                [s * 0.35, margem * 0.4, s * 0.65, margem * 1.8],
                radius=s * 0.05, fill=cor
            )
            cx, cy = s * 0.5, s * 0.48
            r = s * 0.11
            d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=cor, width=largura_linha)
            d.arc(
                [cx - r * 1.7, cy + r * 0.6, cx + r * 1.7, cy + r * 2.6],
                start=200, end=340, fill=cor, width=largura_linha
            )

        elif tipo == "menus":
            # Lista: três linhas horizontais com marcador
            y_pos = [s * 0.28, s * 0.5, s * 0.72]
            for y in y_pos:
                d.ellipse(
                    [margem, y - s * 0.035, margem + s * 0.07, y + s * 0.035],
                    fill=cor
                )
                d.line(
                    [margem + s * 0.16, y, s - margem, y],
                    fill=cor, width=largura_linha
                )

        elif tipo == "acessos":
            # Duas pessoas (círculo + "corpo") sobrepostas
            r = s * 0.15
            cx1, cy = s * 0.36, s * 0.36
            cx2 = s * 0.6
            d.ellipse([cx1 - r, cy - r, cx1 + r, cy + r], outline=cor, width=largura_linha)
            d.arc(
                [cx1 - r * 1.7, cy + r * 0.7, cx1 + r * 1.7, cy + r * 2.9],
                start=200, end=340, fill=cor, width=largura_linha
            )
            r2 = s * 0.15
            d.ellipse(
                [cx2 - r2, cy - r2, cx2 + r2, cy + r2],
                outline=cor, width=largura_linha
            )
            d.arc(
                [cx2 - r2 * 1.7, cy + r2 * 0.7, cx2 + r2 * 1.7, cy + r2 * 2.9],
                start=200, end=340, fill=cor, width=largura_linha
            )

        elif tipo == "sair":
            # Porta com seta apontando para fora
            d.rounded_rectangle(
                [margem, margem, s * 0.55, s - margem],
                radius=s * 0.06, outline=cor, width=largura_linha
            )
            y_meio = s * 0.5
            d.line([s * 0.55, y_meio, s - margem, y_meio], fill=cor, width=largura_linha)
            ponta = s - margem
            d.line([ponta - s * 0.15, y_meio - s * 0.15, ponta, y_meio], fill=cor, width=largura_linha)
            d.line([ponta - s * 0.15, y_meio + s * 0.15, ponta, y_meio], fill=cor, width=largura_linha)

        elif tipo == "calendario":
            d.rounded_rectangle(
                [margem, margem * 1.8, s - margem, s - margem],
                radius=s * 0.08, outline=cor, width=largura_linha
            )
            d.line([margem, s * 0.42, s - margem, s * 0.42], fill=cor, width=largura_linha)
            for x in (s * 0.32, s * 0.68):
                d.line([x, margem * 0.6, x, margem * 2.2], fill=cor, width=largura_linha)

        elif tipo == "pata":
            cx, cy = s * 0.5, s * 0.62
            d.ellipse(
                [cx - s * 0.22, cy - s * 0.18, cx + s * 0.22, cy + s * 0.22],
                fill=cor
            )
            offsets = [(-0.22, -0.30), (-0.08, -0.4), (0.08, -0.4), (0.22, -0.30)]
            for ox, oy in offsets:
                px, py = cx + s * ox, cy + s * oy
                d.ellipse(
                    [px - s * 0.08, py - s * 0.09, px + s * 0.08, py + s * 0.09],
                    fill=cor
                )

        img = img.resize((tamanho, tamanho), Image.LANCZOS)
        foto = ImageTk.PhotoImage(img)

        # Mantém referência para não ser descartada pelo garbage collector.
        self._icones[f"{tipo}_{tamanho}_{cor}"] = foto
        return foto

    def criar_componentes(self):

        # =====================================
        # TOPO: título/subtítulo (esquerda) + cartão de data (direita)
        # =====================================

        self.frm_topo = tk.Frame(
            self.root,
            bg=self.COR_FUNDO
        )

        self.frm_topo.pack(
            fill="x",
            padx=60,
            pady=(40, 0)
        )

        self.frm_topo.grid_columnconfigure(0, weight=1)

        # --- título + subtítulo (coluna esquerda) ---

        self.frm_textos = tk.Frame(self.frm_topo, bg=self.COR_FUNDO)
        self.frm_textos.grid(row=0, column=0, sticky="w")

        self.lbl_titulo = tk.Label(
            self.frm_textos,
            text=(Idioma.t("home_view.mensagem_entrada")),
            font=("Georgia", 34, "bold"),
            bg=self.COR_FUNDO,
            fg=self.COR_TEXTO_ESCURO,
            justify="left"
        )
        self.lbl_titulo.pack(anchor="w")

        self.lbl_subtitulo = tk.Label(
            self.frm_textos,
            text=(Idioma.t("home_view.entrada")),
            font=("Georgia", 18),
            bg=self.COR_FUNDO,
            fg=self.COR_TEXTO_ESCURO
        )
        self.lbl_subtitulo.pack(anchor="w", pady=(8, 0))

        # --- cartão "Hoje é: ..." (coluna direita) ---

        hoje = datetime.date.today()
        texto_data = f"{hoje.day:02d} de {_MESES_PT[hoje.month]} de {hoje.year}"

        self.frm_data = tk.Frame(
            self.frm_topo,
            bg=self.COR_CARTAO,
            padx=26,
            pady=18
        )
        self.frm_data.grid(row=0, column=1, sticky="ne")

        icone_cal = self._criar_icone("calendario", tamanho=40, cor=self.COR_TEXTO_ESCURO)

        tk.Label(
            self.frm_data,
            image=icone_cal,
            bg=self.COR_CARTAO
        ).pack(side="left", padx=(0, 14))

        frm_data_textos = tk.Frame(self.frm_data, bg=self.COR_CARTAO)
        frm_data_textos.pack(side="left")

        tk.Label(
            frm_data_textos,
            text=self._t("home_view.hoje_e", "Hoje é:"),
            font=("Georgia", 13),
            bg=self.COR_CARTAO,
            fg=self.COR_TEXTO_ESCURO,
            justify="left"
        ).pack(anchor="w")

        tk.Label(
            frm_data_textos,
            text=texto_data,
            font=("Georgia", 15, "bold"),
            bg=self.COR_CARTAO,
            fg=self.COR_TEXTO_ESCURO,
            justify="left"
        ).pack(anchor="w")

        # =====================================
        # ÁREA DOS BOTÕES (com a marca d'água atrás)
        # =====================================
        # Usamos um Frame + .place() (em vez de .grid()) porque
        # .place() permite sobrepor widgets: a marca d'água fica
        # "embaixo" e os botões ficam "em cima", na mesma área.

        self.frm_botoes = tk.Frame(
            self.root,
            bg=self.COR_FUNDO
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

        icone_cadastros = self._criar_icone("cadastros", tamanho=46, cor=self.COR_TEXTO_BOTAO)

        self.btn_cadastros = tk.Button(
            self.frm_botoes,
            text=(Idioma.t("home_view.cadastros_basicos")),
            image=icone_cadastros,
            compound="top",
            font=("Georgia", 16, "bold"),
            bg=self.COR_BOTAO,
            fg=self.COR_TEXTO_BOTAO,
            activebackground=self.COR_BOTAO,
            width=220,
            height=140,
            relief="flat",
            bd=0,
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

        icone_menus = self._criar_icone("menus", tamanho=46, cor=self.COR_TEXTO_BOTAO)

        self.btn_menus = tk.Button(
            self.frm_botoes,
            text=(Idioma.t("home_view.menus")),
            image=icone_menus,
            compound="top",
            font=("Georgia", 16, "bold"),
            bg=self.COR_BOTAO,
            fg=self.COR_TEXTO_BOTAO,
            activebackground=self.COR_BOTAO,
            width=220,
            height=140,
            relief="flat",
            bd=0,
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

        icone_acessos = self._criar_icone("acessos", tamanho=46, cor=self.COR_TEXTO_BOTAO)

        self.btn_acessos = tk.Button(
            self.frm_botoes,
            text=(Idioma.t("home_view.acesso")),
            image=icone_acessos,
            compound="top",
            font=("Georgia", 16, "bold"),
            bg=self.COR_BOTAO,
            fg=self.COR_TEXTO_BOTAO,
            activebackground=self.COR_BOTAO,
            width=220,
            height=140,
            relief="flat",
            bd=0,
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

        icone_sair = self._criar_icone("sair", tamanho=46, cor=self.COR_TEXTO_BOTAO)

        self.btn_sair = tk.Button(
            self.frm_botoes,
            text=(Idioma.t("home_view.sair")),
            image=icone_sair,
            compound="top",
            font=("Georgia", 16, "bold"),
            bg=self.COR_BOTAO_SAIR,
            fg=self.COR_TEXTO_BOTAO,
            activebackground=self.COR_BOTAO_SAIR,
            width=220,
            height=140,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.controller.sair
        )

        self.btn_sair.place(
            relx=0.75,
            rely=0.68,
            anchor="center"
        )

        # =====================================
        # RODAPÉ
        # =====================================

        self.frm_rodape = tk.Frame(
            self.root,
            bg=self.COR_FUNDO
        )

        self.frm_rodape.pack(
            fill="x",
            padx=40,
            pady=(0, 20)
        )

        icone_pata_pequena = self._criar_icone("pata", tamanho=26, cor="#C09B7A")

        self.frm_rodape_esquerda = tk.Frame(self.frm_rodape, bg=self.COR_FUNDO)
        self.frm_rodape_esquerda.pack(side="left")

        tk.Label(
            self.frm_rodape_esquerda,
            image=icone_pata_pequena,
            bg=self.COR_FUNDO
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            self.frm_rodape_esquerda,
            text=self._t(
                "home_view.rodape",
                ("Juntos por mais saúde e bem-estar!")
            ),
            font=("Georgia", 13, "italic"),
            bg=self.COR_FUNDO,
            fg=self.COR_TEXTO_ESCURO
        ).pack(side="left")

        # duas patinhas decorativas no canto direito, como na referência
        icone_pata_direita = self._criar_icone("pata", tamanho=24, cor="#C09B7A")

        self.frm_rodape_direita = tk.Frame(self.frm_rodape, bg=self.COR_FUNDO)
        self.frm_rodape_direita.pack(side="right")

        tk.Label(
            self.frm_rodape_direita, image=icone_pata_direita, bg=self.COR_FUNDO
        ).pack(side="left", padx=4)

        tk.Label(
            self.frm_rodape_direita, image=icone_pata_direita, bg=self.COR_FUNDO
        ).pack(side="left", padx=4)

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
            bg=self.COR_FUNDO,
            bd=0,
            highlightthickness=0
        )

        self.lbl_marca_dagua.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )