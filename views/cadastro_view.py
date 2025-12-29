import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from tkinter import ttk
from controls.cadastrar_destinatarios import cmd_cadastrar_email, listar_cadastro

class CadastroView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        #Controle de estado para as alterações de cadastro
        self.modo_edicao = False
        self.cdc_em_edicao = None

        # =========================
        # CONFIGURAÇÃO GERAL
        # =========================
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
        lbl_titulo.grid(row=0, column=0, sticky="w", padx=20, pady=(10, 5))

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

        self.entry_email.grid(row=3, column=0, sticky="ew", padx=10, pady=(0, 5))
        self.entry_responsavel.grid(row=3, column=1, sticky="ew", padx=10, pady=(0, 5))

        # ---- Linha 3 (AÇÃO FORMULÁRIO)
        form_action_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        form_action_frame.grid(
            row=4,
            column=0,
            columnspan=2,
            sticky="e",
            padx=10,
            pady=(5, 10)
        )

        self.btn_cadastrar = ctk.CTkButton(
            form_action_frame,
            text="Cadastrar",
            width=140,
            height=40,
            command=self.cadastrar
        )
        self.btn_cadastrar.grid(row=0, column=0)

        # =========================
        # CARD - TABELA
        # =========================
        table_frame = ctk.CTkFrame(self, corner_radius=12)
        table_frame.grid(row=2, column=0, sticky="nsew", padx=20, pady=(0, 20))

        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_rowconfigure(1, weight=0)

        # ---- Estilo da tabela
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

        # ---- AÇÕES DA TABELA
        table_action_frame = ctk.CTkFrame(table_frame, fg_color="transparent")
        table_action_frame.grid(
            row=1,
            column=0,
            sticky="e",
            padx=10,
            pady=(0, 10)
        )

        self.btn_editar = ctk.CTkButton(
            table_action_frame,
            text="Editar",
            width=100,
            fg_color="#FFA500",
            command=self.editar,
            state="disabled"
        )
        self.btn_editar.grid(row=0, column=0, padx=(0, 10))

        self.btn_excluir = ctk.CTkButton(
            table_action_frame,
            text="Excluir",
            width=100,
            fg_color="#D32F2F",
            command=self.excluir,
            state="disabled"
        )
        self.btn_excluir.grid(row=0, column=1)

        # Bind seleção da tabela
        self.tabela.bind("<<TreeviewSelect>>", self.on_select)
        
        self.carregar_tabela()
    # =========================
    # MÉTODOS
    # =========================
    def cadastrar(self):
        dados = {
            "cdc": self.entry_cdc.get().strip(),
            "descricao": self.entry_descricao.get().strip(),
            "email": self.entry_email.get().strip(),
            "responsavel": self.entry_responsavel.get().strip()
        }

        if self.modo_edicao:
            cmd_cadastrar_email(self.cdc_em_edicao, dados)
            CTkMessagebox(
                title="Sucesso",
                message="Dados alterados com sucesso!",
                icon="check"
            )

        else:
            cmd_cadastrar_email(dados)
        
        self.sair_modo_edicao()
        self.carregar_tabela()
        self.limpar_formulario()
    
    def limpar_formulario(self):
        self.entry_cdc.delete(0, "end")
        self.entry_descricao.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.entry_responsavel.delete(0, "end")

    def carregar_tabela(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        registros = listar_cadastro()

        for registro in registros:
            self.tabela.insert(
                "",
                "end",
                values=(
                    registro.get("cdc"),
                    registro.get("descricao"),
                    registro.get("email"),
                    registro.get("responsavel"),
                )
            )

    def editar(self):
        print("Editar")

       

    def excluir(self):
        print("Excluir registro")

    def on_select(self, event):
        if self.tabela.selection():
            self.btn_editar.configure(state="normal")
            self.btn_excluir.configure(state="normal")

    def sair_modo_edicao(self):
        self.modo_edicao = False
        self.cdc_em_edicao = None

        self.entry_cdc.configure(state="normal")
        self.btn_cadastrar.configure(text="Cadastrar")
