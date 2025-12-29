import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog
from tkinter import ttk
from controls.validar_arquivos import validar_arquivos_por_cdc, montar_linhas_treeview
from controls.preparar_email import preparar_lista_emails
from controls.preparar_email import preparar_emails_outlook

class ImportarArquivoView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # =========================
        # CONFIGURAÇÃO GERAL
        # =========================
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # =========================
        # TÍTULO
        # =========================
        lbl_titulo = ctk.CTkLabel(
            self,
            text="Importar Arquivos para Envio",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        lbl_titulo.grid(row=0, column=0, sticky="w", padx=20, pady=(15, 5))

        # =========================
        # FRAME PRINCIPAL
        # =========================
        self.form_frame = ctk.CTkFrame(self, corner_radius=12)
        self.form_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)

        self.form_frame.grid_columnconfigure(0, weight=1)
        self.form_frame.grid_rowconfigure(1, weight=0)

        # =========================
        # CAMPOS
        # =========================

        self._criar_caminho_arquivo()
        self._criar_treeview()
        self._btn_preparar_email()

        # =========================
        # BOTÕES DO FORMULÁRIO
        # =========================


    # ======================================================
    # CRIAÇÃO DOS CAMPOS E BOTÕES
    # ======================================================
    def _criar_label(self, texto, row):
        label = ctk.CTkLabel(self.form_frame, text=texto)
        label.grid(row=row, column=0, sticky="w", padx=10, pady=(10, 0))

    def _criar_caminho_arquivo(self):
        self._criar_label("Arquivos para importação:", 0)

        self.caminho_arquivos = ctk.CTkEntry(self.form_frame)
        self.caminho_arquivos.grid(
            row=1, column=0, sticky="ew", padx=10
        )

        self.btn_importar_arquivo = ctk.CTkButton(
            self.form_frame,
            text="Procurar",
            command=self.abrir_pasta
        )

        self.btn_importar_arquivo.grid(
            row=1, column=1, sticky="e", padx=(5,10), pady=10
        )

        self.btn_validar_arquivos = ctk.CTkButton(
            self.form_frame,
            text="Validar",
            command=self.validar_arquivos
        )
        self.btn_validar_arquivos.grid(
            row=1, column=2, sticky='e', padx=(5, 10), pady=10
        )
    
    def _criar_treeview(self):
        colunas = ("cdc", "email", "arquivo", "status")

        # =========================
        # ESTILO
        # =========================
        style = ttk.Style()

        style.theme_use("default")  # importante no Windows

        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 11, "bold"),
            background="#E5E7EB",
            foreground="#111827"
        )

        style.configure(
            "Treeview",
            font=("Segoe UI", 10),
            rowheight=28,
            background="white",
            fieldbackground="white",
            foreground="#111827"
        )

        style.map(
            "Treeview",
            background=[("selected", "#2563EB")],
            foreground=[("selected", "white")]
        )

        self.tree = ttk.Treeview(
            self.form_frame,
            columns=colunas, 
            show="headings",
            height=10
        )
        
        self.tree.tag_configure("ok", foreground="#14BE52")    
        self.tree.tag_configure("erro", foreground="#D21111")
        self.tree.tag_configure("alerta", foreground="#92400E")

        self.tree.heading("cdc", text="CDC")
        self.tree.heading("email", text="E-mail")
        self.tree.heading("arquivo", text="Arquivo")
        self.tree.heading("status", text="Status")

        self.tree.column("cdc", width=80, anchor="center")
        self.tree.column("email", width=200, anchor="center")
        self.tree.column("arquivo", width=280, anchor="center")
        self.tree.column("status", width=160, anchor="center")

        self.tree.grid(
            row=2, column=0, columnspan=3,
            sticky="nsew", padx=10, pady=(10, 5) 
        )

    def _btn_preparar_email(self):
        self.btn_preparar_email = ctk.CTkButton(
            self.form_frame,
            text="Preparar E-mail",
            command=self.preparar_envio
        )

        self.btn_preparar_email.grid(
            row=3, column=0, columnspan=3, sticky="e", padx=(5,10), pady=10
        )
    # ======================================================
    # SEÇÃO DE MÉTODOS
    # ======================================================
    
    def abrir_pasta(self):
        caminho = filedialog.askdirectory(
            title="Selecione a pasta",
        )

        if caminho:
            self.caminho_arquivos.delete(0, "end")
            self.caminho_arquivos.insert(0, caminho)

    def validar_arquivos(self):
        caminho = self.caminho_arquivos.get()

        if not caminho:
            CTkMessagebox(
                title="Erro",
                message="Selecione uma pasta primeiro.",
                icon="cancel"
            )        
            return 

        self.resultado_validacao = validar_arquivos_por_cdc(caminho)

        #Preencher os dados populados na treeview.
        linhas = montar_linhas_treeview(self.resultado_validacao)
        self.preencher_treeview(linhas)
        print(linhas)

    def preencher_treeview(self, dados):

        for item in self.tree.get_children():
            self.tree.delete(item)

        for linha in dados:
            if linha["status"] == "ok":
                tag = "ok"
            elif linha["status"] in ("SEM E-MAIL", "SEM ARQUIVO"):
                tag = "alerta"
            else:
                tag = "erro"
            
            self.tree.insert(
                "",
                "end",
                values=(
                    linha["cdc"],
                    linha["email"],
                    linha["arquivo"],
                    linha["status"]
                ),
                tags=(tag,)
            )
    
    def preparar_envio(self):
        if not hasattr(self, "resultado_validacao"):
            CTkMessagebox(
                title="Atenção",
                message="Valide os arquivos antes de preparar os e-mails.",
                icon="warning"
            )
            return

        emails = preparar_lista_emails(self.resultado_validacao)
        preparar_emails_outlook(emails)

        CTkMessagebox(
            title="Sucesso",
            message="E-mails preparados no Outlook com sucesso.",
            icon="check"
        )