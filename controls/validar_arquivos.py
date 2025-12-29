from controls.importar_arquivos import importar_arquivos_pasta, ler_nome_arquivo
from controls.cadastrar_destinatarios import carregar_cadastro_emails


def validar_arquivos_por_cdc(caminho_pasta):

    print("\n[DEBUG] Iniciando validação de arquivos")
    print(f"[DEBUG] Pasta informada: {caminho_pasta}")

    arquivos = importar_arquivos_pasta(caminho_pasta)
    cadastro = carregar_cadastro_emails()

    print(f"[DEBUG] Total de arquivos encontrados na pasta: {len(arquivos)}")
    print(f"[DEBUG] Total de CDCs cadastrados: {len(cadastro)}")

    resultado = {}
    arquivos_sem_cdc = []
    arquivos_cdc_sem_email = []
    cdc_sem_arquivo = set(cadastro.keys())

    for arquivo in arquivos:
        print("\n[DEBUG] ----------------------------------")
        print(f"[DEBUG] Processando arquivo: {arquivo.name}")

        cdc = ler_nome_arquivo(arquivo)
        print(f"[DEBUG] CDC extraído: {cdc}")

        if not cdc:
            print("[DEBUG] ❌ Arquivo SEM CDC identificado")
            arquivos_sem_cdc.append(arquivo.name)
            continue

        if cdc not in cadastro:
            print("[DEBUG] ⚠️ CDC encontrado, mas NÃO cadastrado")
            arquivos_cdc_sem_email.append({
                "cdc": cdc,
                "arquivo": arquivo.name
            })
            continue

        print("[DEBUG] ✅ CDC válido e cadastrado")

        resultado.setdefault(cdc, {
            "email": cadastro[cdc]["email"],
            "arquivo": []
        })

        resultado[cdc]["arquivo"].append(arquivo)
        cdc_sem_arquivo.discard(cdc)

    print("\n[DEBUG] ===== RESUMO FINAL =====")
    print(f"[DEBUG] Arquivos válidos: {sum(len(v['arquivo']) for v in resultado.values())}")
    print(f"[DEBUG] Arquivos sem CDC: {len(arquivos_sem_cdc)}")
    print(f"[DEBUG] Arquivos com CDC sem e-mail: {len(arquivos_cdc_sem_email)}")
    print(f"[DEBUG] CDCs sem arquivo: {len(cdc_sem_arquivo)}")

    return {
        "valido": resultado,
        "cdc_sem_arquivo": list(cdc_sem_arquivo),
        "arquivo_sem_cdc": arquivos_sem_cdc,
        "cdc_sem_email": arquivos_cdc_sem_email
    }

def montar_linhas_treeview(dados):
    linhas = []

    #CDCs com arquivo
    for cdc, info in dados["valido"].items():
        for arquivo in info["arquivo"]:
            linhas.append({
                "cdc": cdc,
                "email": info["email"],
                "arquivo": arquivo.name,
                "status": "ok"
            })
    
    # 2️⃣ Arquivos com CDC identificado, mas sem e-mail cadastrado
    for item in dados.get("cdc_sem_email", []):
        linhas.append({
            "cdc": item["cdc"],
            "email": "Não cadastrado",
            "arquivo": item["arquivo"],
            "status": "SEM E-MAIL"
        })

    # 3️⃣ CDCs que têm e-mail mas não têm arquivo
    for cdc in dados["cdc_sem_arquivo"]:
        linhas.append({
            "cdc": cdc,
            "email": "—",
            "arquivo": "Não encontrado",
            "status": "SEM ARQUIVO"
        })

    # 4️⃣ Arquivos sem CDC no nome
    for nome_arquivo in dados["arquivo_sem_cdc"]:
        linhas.append({
            "cdc": "—",
            "email": "—",
            "arquivo": nome_arquivo,
            "status": "CDC NÃO IDENTIFICADO"
        })

    return linhas