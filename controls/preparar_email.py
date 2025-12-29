#Módulo criado para preparar o envio de emails válidos para o outlook

import win32com.client as win32
import pythoncom
from pathlib import Path
from controls.salvar_email_padrao import carregar_email_cadastrado


def preparar_lista_emails(resultado_validacao):
    """
    Monta a lista de e-mails pronta para o Outlook
    """
    modelo = carregar_email_cadastrado()
    emails = []

    for cdc, dados in resultado_validacao['valido'].items():
        emails.append({
            "de": modelo.get("de"),
            "to": dados['email'],
            "subject": modelo.get("assunto"),
            "body": modelo.get("corpo"),
            "attachments": dados["arquivo"]
        })

    return emails


def preparar_emails(lista, pasta_arquivos, assunto, corpo):
    """
    Prepara os e-mails para envio.
    Não envia — apenas monta os dados.
    """
    emails_preparados = []

    pasta_arquivos = Path(pasta_arquivos)

    for item in lista:
        if item["status"] != "OK":
            continue

        email = item["email"]
        arquivo = pasta_arquivos / item["arquivo"]

        if not arquivo.exists():
            continue

        if email not in emails_preparados:
            emails_preparados[email] = {
                "to": email,
                "subject": assunto,
                "body": corpo,
                "attachments": []
            }
        
        emails_preparados[email]["attachments"].append(arquivo)

    return list(emails_preparados.values())

def preparar_emails_outlook(emails):
    """
    Cria e-mails no Outlook com anexos e deixa na Caixa de Saída/Rascunhos.
    NÃO envia automaticamente.
    """
    pythoncom.CoInitialize()
    try:
        outlook = win32.Dispatch("Outlook.Application")
        namespace = outlook.GetNamespace("MAPI")

        for email in emails:
            mail = outlook.CreateItem(0)

            if email.get("de"):
                mail.SentOnBehalfOfName = email["de"]

            mail.To = email["to"]
            mail.Subject = email["subject"]
            mail.Body = email["body"]

            for anexo in email["attachments"]:
                mail.Attachments.Add(str(anexo))

            mail.Save()  # fica em Rascunhos
        
    finally:
        pythoncom.CoUninitialize()