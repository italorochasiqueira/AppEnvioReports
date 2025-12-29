import json
from pathlib import Path
from controls.caminho_relativo import caminho_relativo_app

def cmd_cadastrar_email(dados: dict):
    validar_dados(dados)
    salvar_json(dados)

def validar_dados(dados):
    campos_obrigatorios = ["cdc", "descricao", "email", "responsavel"]

    for campo in campos_obrigatorios:
        print(f"[DEBUG] Campo encontrado: {campo}")
        if not dados.get(campo):
            raise ValueError(f"O campo '{campo}' é obrigatório!")

def salvar_json(novo_registro):
    caminho_base = caminho_relativo_app()
    caminho_arquivo = caminho_base / "models" / "cadastro_email.json"
    print(f"[DEBUG] Caminho encontrado para registro dos dados: {caminho_arquivo}")

    if caminho_arquivo.exists():
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            registros = json.load(f)
    else:
        registros = []
    
    registros.append(novo_registro)
    print(f"[INFO] Registros cadastrados na base: {registros}")

    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump(registros, f, ensure_ascii=False, indent=4)

def listar_cadastro():
    caminho_base = caminho_relativo_app()
    caminho_arquivo = caminho_base / "models" / "cadastro_email.json"
    print(f"[DEBUG] Caminho dos dados registrados: {caminho_arquivo}")

    if not caminho_arquivo.exists():
        return []
    
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

def carregar_cadastro_emails():

    dados = listar_cadastro()

    return {
        item['cdc']: item
        for item in dados
    }

