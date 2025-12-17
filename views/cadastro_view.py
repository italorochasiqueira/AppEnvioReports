import customtkinter as ctk
from tkinter import ttk

class CadastroView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure((0,1,2,3), weight=1)

        # Título
        lbl_titulo = ctk.CTkLabel(
        self,
        text="Cadastro de E-mails",
        font=ctk.CTkFont(size=18, weight="bold")
        )
        lbl_titulo.grid(row=0, column=0, columnspan=4, pady=(5, 5))

        # Campos de entrada
        ctk.CTkLabel(self, text="CDC", 
                     font=ctk.CTkFont(size=10, weight="bold")
                    ).grid(row=1, column=0, sticky="w", padx=10)
        self.entry_cdc = ctk.CTkEntry(self)
        self.entry_cdc.grid(row=2, column=0, padx=10, pady=(0,10), sticky="ew")


        ctk.CTkLabel(self, text="Descrição",
                     font=ctk.CTkFont(size=10, weight="bold")
                    ).grid(row=1, column=1, sticky="w", padx=10)
        self.entry_descricao = ctk.CTkEntry(self)
        self.entry_descricao.grid(row=2, column=1, padx=10, pady=(0,10), sticky="ew")


        ctk.CTkLabel(self, text="E-mail",
                     font=ctk.CTkFont(size=10, weight="bold")
                    ).grid(row=1, column=2, sticky="w", padx=10)
        self.entry_email = ctk.CTkEntry(self)
        self.entry_email.grid(row=2, column=2, padx=10, pady=(0,10), sticky="ew")


        ctk.CTkLabel(self, text="Responsável",
                     font=ctk.CTkFont(size=10, weight="bold")
                    ).grid(row=1, column=3, sticky="w", padx=10)
        self.entry_responsavel = ctk.CTkEntry(self)
        self.entry_responsavel.grid(row=2, column=3, padx=10, pady=(0,10), sticky="ew")


        # Botões
        self.btn_cadastrar = ctk.CTkButton(self, text="Cadastrar", command=self.cadastrar)
        self.btn_cadastrar.grid(row=3, column=0, pady=10)


        self.btn_editar = ctk.CTkButton(self, text="Editar", fg_color="#FFA500", command=self.editar)
        self.btn_editar.grid(row=3, column=1, pady=10)


        self.btn_excluir = ctk.CTkButton(self, text="Excluir", fg_color="red", command=self.excluir)
        self.btn_excluir.grid(row=3, column=2, pady=10)

        # Tabela
        style = ttk.Style()
        style.configure(
            "Cadastro.Treeview",
            font=("Segoe UI", 10),
            rowheight=24
        )

        style.configure(
            "Cadastro.Treeview.Heading",
            font=("Segoe UI", 10, "bold")
        )

        self.tabela = ttk.Treeview(
        self,
        columns=("cdc", "descricao", "email", "responsavel"),
        show="headings",
        style="Cadastro.Treeview"
        )

        self.tabela.heading("cdc", text="CDC")
        self.tabela.heading("descricao", text="Descrição")
        self.tabela.heading("email", text="E-mail")
        self.tabela.heading("responsavel", text="Responsável")


        self.tabela.grid(row=4, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)


        self.grid_rowconfigure(4, weight=1)


    # Métodos (placeholder)
    def cadastrar(self):
        print("Cadastrar registro")


    def editar(self):
        print("Editar registro")


    def excluir(self):
        print("Excluir registro")