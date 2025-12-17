from pathlib import Path

def caminho_relativo_app():
    '''Função para caminho relativo do programa'''
    try:
        caminho_relativo = Path(__file__).resolve(strict=True).parent.parent
        print(f"[DEBUG] O caminho relativo acessado é: {caminho_relativo}")
        return caminho_relativo
    except NameError:
        print("[DEBUG] __file__ não está definido. A função pode estar a ser executada interativamente.")
        return Path.cwd() 


