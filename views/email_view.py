# Tela de E-mail padrão que é enviado
# Construção de um campo para assunto e corpo do E-mail
# Os dados são salvos em json na pasta models

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from controls.salvar_email_padrao import salvar_modelo_email_json, carregar_email_cadastrado

class EmailView(ctk.CTkFrame):
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
            text="E-mail de Envio",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        lbl_titulo.grid(row=0, column=0, sticky="w", padx=20, pady=(15, 5))

        # =========================
        # FRAME PRINCIPAL
        # =========================
        self.form_frame = ctk.CTkFrame(self, corner_radius=12)
        self.form_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)

        self.form_frame.grid_columnconfigure(0, weight=1)
        self.form_frame.grid_rowconfigure(5, weight=1)

        # =========================
        # CAMPOS
        # =========================
        self._criar_campo_de()
        self._criar_campo_assunto()
        self._criar_campo_corpo()

        # =========================
        # BOTÕES DO FORMULÁRIO
        # =========================
        self.btn_salvar = ctk.CTkButton(
            self.form_frame,
            text="Salvar modelo de e-mail",
            command=self.salvar_modelo
        )
        self.btn_salvar.grid(
            row=6, column=0, sticky="e", padx=10, pady=(10, 15)
        )

        #Chamar função para preencher dados do email padrão já cadastrado.
        self.preencher_dados_email()

    # ======================================================
    # MÉTODOS DE CRIAÇÃO DOS CAMPOS
    # ======================================================
    def _criar_label(self, texto, row):
        label = ctk.CTkLabel(self.form_frame, text=texto)
        label.grid(row=row, column=0, sticky="w", padx=10, pady=(10, 0))

    def _criar_campo_de(self):
        self._criar_label("De:", 0)

        self.entry_de = ctk.CTkEntry(self.form_frame)
        self.entry_de.grid(
            row=1, column=0, sticky="ew", padx=10
        )

    def _criar_campo_assunto(self):
        self._criar_label("Assunto do e-mail:", 2)

        self.entry_assunto = ctk.CTkEntry(self.form_frame)
        self.entry_assunto.grid(
            row=3, column=0, sticky="ew", padx=10
        )

    def _criar_campo_corpo(self):
        self._criar_label("Corpo do e-mail:", 4)

        self.txt_corpo = ctk.CTkTextbox(self.form_frame)
        self.txt_corpo.grid(
            row=5, column=0, sticky="nsew", padx=10, pady=(0, 10)
        )

    # ======================================================
    # SEÇÃO PARA OBTER DADOS DA TELA
    # ======================================================
    def obter_dados(self):
        return {
            "de": self.entry_de.get(),
            "assunto": self.entry_assunto.get(),
            "corpo": self.txt_corpo.get("1.0", "end").strip()
        }

    def salvar_modelo(self):
        dados = self.obter_dados()
        salvar_modelo_email_json(dados)
        CTkMessagebox (
            title="Sucesso",
            message="Modelo de e-mail salvo com sucesso.",
            icon="check"
        )

    #PREENCHER OS CAMPOS COM OS DADOS JÁ CADASTRADOS
    def preencher_dados_email(self):
        dados_email = carregar_email_cadastrado()

        if not dados_email:
            return
        
        self.entry_de.delete(0, "end")
        self.entry_de.insert(0, dados_email.get("de", ""))

        self.entry_assunto.delete(0, "end")
        self.entry_assunto.insert(0, dados_email.get("assunto", ""))

        self.txt_corpo.delete("1.0", "end")
        self.txt_corpo.insert("1.0", dados_email.get("corpo", ""))
