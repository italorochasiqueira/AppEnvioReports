from pathlib import Path
import re

def importar_arquivos_pasta(caminho):
    '''Retorna todos os arquivos da pasta'''
    print(f"[DEBUG] Caminho recebido: {caminho}")

    pasta = Path(caminho)
    print(f"[DEBUG] Pasta existe? {pasta.exists()} | É dir? {pasta.is_dir()}")

    arquivos = [arquivo for arquivo in pasta.iterdir() if arquivo.is_file()]

    print(f"[DEBUG] Total de arquivos encontrados: {len(arquivos)}")
    for a in arquivos:
        print(f" - {a.name}")

    return arquivos

def ler_nome_arquivo(arquivo: Path):
    """
    Extrai o CDC do nome do arquivo.
    Retorna None se não encontrar.
    """
    padrao = r'^([A-Z]{3})\b'

    match = re.match(padrao, arquivo.stem)

    if match:
        return match.group(1)
    
    return None