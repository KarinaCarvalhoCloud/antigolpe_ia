import re
import requests
import idna # Biblioteca essencial para homógrafos

# NOTA: Para funcionar, você precisa ter as bibliotecas instaladas: 
# pip install requests idna

def verificar_homografos(url_original):
    """
    Verifica a URL em busca de ataques de homógrafos usando Punycode.
    Retorna True se for suspeita, False caso contrário.
    """
    dominio = url_original.split('//')[-1].split('/')[0]
    
    # 1. Tenta decodificar o Punycode (usado para caracteres não-latinos)
    try:
        dominio_decoded = idna.decode(dominio)
        
        # 2. Verifica se a decodificação resultou em caracteres não-ASCII
        # Se os caracteres decodificados forem diferentes dos originais, 
        # e contiverem caracteres não-latinos, é um forte indicador de ataque homográfico.
        if dominio_decoded != dominio:
            # Verifica se algum caractere no domínio decodificado não é um caractere latino comum.
            # Este regex verifica por caracteres que não são letras latinas (a-z, A-Z), números (0-9), ou hifens.
            if re.search(r'[^\w\.-]', dominio_decoded):
                return True, dominio_decoded

    except idna.IDNAError:
        # Ignora erros de formato IDNA inválido
        pass
        
    return False, dominio

def verificar_url(url):
    """
    Verifica a URL em busca de padrões de risco (IPs, encurtadores, homógrafos, redirecionamentos).
    """
    resultado = {
        "url": url,
        "risco": 0,
        "motivos": []
    }
    
    # --- 1. Verificação de Homógrafos (Nova Adição) ---
    is_homografo, dominio_decoded = verificar_homografos(url)
    if is_homografo:
        resultado["risco"] += 40
        resultado["motivos"].append(f"⚠️ Risco de **Ataque Homográfico**! O domínio se decodifica para: **{dominio_decoded}**")


    # --- 2. Detecção de IP na URL ---
    # Nota: A regex foi corrigida para garantir 4 blocos de números.
    if re.match(r"https?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", url):
        resultado["risco"] += 30
        resultado["motivos"].append("URL usa **endereço IP** — comum em phishing.")

    # --- 3. Detecção de encurtadores ---
    encurtadores = ["bit.ly", "tinyurl", "rb.gy", "cutt.ly", "is.gd"]
    if any(e in url for e in encurtadores):
        resultado["risco"] += 20
        resultado["motivos"].append("URL **encurtada** — pode ocultar destino real.")

    # --- 4. Verificação de Redirecionamento (Análise HEAD) ---
    try:
        response = requests.head(url, timeout=5, allow_redirects=True)
        # Se a URL final for diferente da original e não for um encurtador que já deu risco:
        if response.url != url and not any(e in url for e in encurtadores):
            resultado["risco"] += 10
            resultado["motivos"].append("Redirecionamento detectado para: " + response.url)
            
    except requests.exceptions.RequestException as e:
        # Adiciona o erro apenas se não for um risco já detectado
        if not resultado["motivos"]:
             resultado["motivos"].append(f"Não foi possível conectar ao domínio: {str(e)}")

    return resultado