import customtkinter as ctk

from views.cadastro_view import CadastroView
from views.email_view import EmailView
from views.importar_arquivo_view import ImportarArquivoView

ctk.set_appearance_mode("System")  # System, Dark, Light
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da janela
        self.title("Aplicativo de Envio de E-mails")
        self.geometry("900x600")
        self.minsize(800, 500)

        # Layout base (sidebar + conteúdo)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.criar_sidebar()
        self.criar_area_conteudo()

    def criar_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="ns")
        self.sidebar.grid_rowconfigure(4, weight=1)

        lbl_logo = ctk.CTkLabel(
            self.sidebar,
            text="Postalis - CPF",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        lbl_logo.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.btn_areas = ctk.CTkButton(
            self.sidebar,
            text="Cadastro",
            command=self.tela_areas
        )
        
        self.btn_areas.grid(row=1, column=0, padx=20, pady=10)

        self.btn_envio = ctk.CTkButton(
            self.sidebar,
            text="E-mail",
            command=self.tela_envio
        )
        self.btn_envio.grid(row=2, column=0, padx=20, pady=10)

        self.btn_config = ctk.CTkButton(
            self.sidebar,
            text="Importar arquivos",
            command=self.tela_config
        )
        self.btn_config.grid(row=3, column=0, padx=20, pady=10)

        self.btn_sair = ctk.CTkButton(
            self.sidebar,
            text="Sair",
            fg_color="red",
            hover_color="#8b0000",
            command=self.destroy
        )
        self.btn_sair.grid(row=5, column=0, padx=20, pady=20)

    def criar_area_conteudo(self):
        self.conteudo = ctk.CTkFrame(self)
        self.conteudo.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.conteudo.grid_columnconfigure(0, weight=1)
        self.conteudo.grid_rowconfigure(0, weight=0)
        self.conteudo.grid_rowconfigure(1, weight=1)

        self.lbl_home = ctk.CTkLabel(
            self.conteudo,
            text="Bem-vindo ao Aplicativo de Envio de E-mails\n\n"
                 "Utilize o menu lateral para iniciar.",
            font=ctk.CTkFont(size=16)
        )
        self.lbl_home.grid(row=0, column=0)

    def limpar_conteudo(self):
        for widget in self.conteudo.winfo_children():
            widget.destroy()

    def tela_areas(self):
        self.limpar_conteudo()
        view = CadastroView(self.conteudo)
        view.grid(row=1, column=0, sticky='nsew')

    def tela_envio(self):
        self.limpar_conteudo()
        view = EmailView(self.conteudo)
        view.grid(row=1, column=0, sticky='nsew')

    def tela_config(self):
        self.limpar_conteudo()
        view = ImportarArquivoView(self.conteudo)
        view.grid(row=1, column=0, sticky='nsew')

