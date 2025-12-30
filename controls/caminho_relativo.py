from pathlib import Path
import sys

def caminho_relativo_app():
    """
    Retorna o diretório base do app:
    - Em desenvolvimento: pasta do projeto
    - Em executável (PyInstaller): pasta temporária (_MEIPASS)
    """
    if getattr(sys, 'frozen', False):
        return Path(sys._MEIPASS)
    else:
        return Path(__file__).resolve().parent.parent

def caminho_relativo_figuras(caminho):
    return caminho_relativo_app() / caminho

