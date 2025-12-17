import customtkinter as ctk
from tkinter import ttk


class CadastroView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Configuração geral
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # =========================
        # TÍTULO
        # =========================
        lbl_titulo = ctk.CTkLabel(
            self,
            text="Cadastro de E-mails",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        lbl_titulo.grid(row=0, column=0, pady=(10, 5), sticky="w", padx=20)

        # =========================
        # CARD - FORMULÁRIO
        # =========================
        form_frame = ctk.CTkFrame(self, corner_radius=12)
        form_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=10)

        form_frame.grid_columnconfigure(0, weight=1)
        form_frame.grid_columnconfigure(1, weight=1)

        # ---- Linha 1
        ctk.CTkLabel(form_frame, text="CDC").grid(
            row=0, column=0, sticky="w", padx=10, pady=(10, 0)
        )
        ctk.CTkLabel(form_frame, text="Descrição").grid(
            row=0, column=1, sticky="w", padx=10, pady=(10, 0)
        )

        self.entry_cdc = ctk.CTkEntry(form_frame)
        self.entry_descricao = ctk.CTkEntry(form_frame)

        self.entry_cdc.grid(row=1, column=0, sticky="ew", padx=10)
        self.entry_descricao.grid(row=1, column=1, sticky="ew", padx=10)

        # ---- Linha 2
        ctk.CTkLabel(form_frame, text="E-mail").grid(
            row=2, column=0, sticky="w", padx=10, pady=(10, 0)
        )
        ctk.CTkLabel(form_frame, text="Responsável").grid(
            row=2, column=1, sticky="w", padx=10, pady=(10, 0)
        )

        self.entry_email = ctk.CTkEntry(form_frame)
        self.entry_responsavel = ctk.CTkEntry(form_frame)

        self.entry_email.grid(row=3, column=0, sticky="ew", padx=10, pady=(0, 10))
        self.entry_responsavel.grid(row=3, column=1, sticky="ew", padx=10, pady=(0, 10))

        # =========================
        # BOTÕES
        # =========================
        btn_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        btn_frame.grid(row=4, column=0, columnspan=2, sticky="e", padx=10, pady=10)

        self.btn_cadastrar = ctk.CTkButton(
            btn_frame, text="Cadastrar", width=120, command=self.cadastrar
        )
        self.btn_cadastrar.grid(row=0, column=0, padx=(0, 10))

        self.btn_editar = ctk.CTkButton(
            btn_frame, text="Editar", width=100, fg_color="#FFA500", command=self.editar
        )
        self.btn_editar.grid(row=0, column=1, padx=(0, 10))

        self.btn_excluir = ctk.CTkButton(
            btn_frame, text="Excluir", width=100, fg_color="#D32F2F", command=self.excluir
        )
        self.btn_excluir.grid(row=0, column=2)

        # =========================
        # CARD - TABELA
        # =========================
        table_frame = ctk.CTkFrame(self, corner_radius=12)
        table_frame.grid(row=2, column=0, sticky="nsew", padx=20, pady=(0, 20))

        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

        # Estilo da tabela
        style = ttk.Style()
        style.configure(
            "Cadastro.Treeview",
            font=("Segoe UI", 10),
            rowheight=26
        )
        style.configure(
            "Cadastro.Treeview.Heading",
            font=("Segoe UI", 10, "bold")
        )

        self.tabela = ttk.Treeview(
            table_frame,
            columns=("cdc", "descricao", "email", "responsavel"),
            show="headings",
            style="Cadastro.Treeview"
        )

        self.tabela.heading("cdc", text="CDC", anchor="center")
        self.tabela.heading("descricao", text="Descrição", anchor="center")
        self.tabela.heading("email", text="E-mail", anchor="center")
        self.tabela.heading("responsavel", text="Responsável", anchor="center")

        self.tabela.column("cdc", width=80, anchor="center")
        self.tabela.column("descricao", width=200)
        self.tabela.column("email", width=220)
        self.tabela.column("responsavel", width=180)

        self.tabela.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    # =========================
    # MÉTODOS
    # =========================
    def cadastrar(self):
        print("Cadastrar registro")

    def editar(self):
        print("Editar registro")

    def excluir(self):
        print("Excluir registro")
