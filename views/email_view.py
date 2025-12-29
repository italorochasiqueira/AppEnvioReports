import customtkinter as ctk
from tkinter import ttk

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
        lbl_titulo.grid(row=0, column=0, sticky="w", padx=20, pady=(10, 5))

        # =========================
        # CONTEÚDO PRINCIPAL
        # =========================
        conteudo_frame = ctk.CTkFrame(self, corner_radius=12)
        conteudo_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)

        conteudo_frame.grid_columnconfigure(0, weight=1)
        conteudo_frame.grid_rowconfigure(0, weight=1)

        # Aqui você pode adicionar mais widgets ao conteudo_frame conforme necessário
