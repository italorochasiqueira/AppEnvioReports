import json
from pathlib import Path
from controls.caminho_relativo import caminho_relativo_app

def salvar_modelo_email_json(novo_registro: dict):
    """
    Salva ou atualiza o modelo único de e-mail.
    Sempre sobrescreve o arquivo existente.
    """
    caminho_base = caminho_relativo_app()
    caminho_arquivo = caminho_base / "models" / "modelo_email.json"

    caminho_arquivo.parent.mkdir(parents=True, exist_ok=True)
    print(f"[DEBUG] Caminho encontrado para registro dos dados: {caminho_arquivo}")

    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump(novo_registro, f, ensure_ascii=False, indent=4)

    print("[INFO] Modelo de e-mail salvo/atualizado com sucesso.")


def carregar_email_cadastrado():
    caminho_base = caminho_relativo_app()
    caminho_arquivo = caminho_base / "models" / "modelo_email.json"

    if not caminho_arquivo.exists():
        return {}

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Arquivo existe, mas está vazio ou inválido
        return {}