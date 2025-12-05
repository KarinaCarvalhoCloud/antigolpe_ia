import re
from ai_engine import analisar_mensagem_com_ia

def analisar_mensagem(texto):
    """
    Realiza uma análise técnica inicial e envia o texto para análise da IA.
    """
    indicadores = {
        "pede_dinheiro": False,
        "palavras_urgencia": [],
        "links_encontrados": []
    }

    # 1. Detecção de palavras de urgência
    palavras_urgencia = ["urgente", "agora", "imediato", "última chance", "corre", "pendente"]
    for palavra in palavras_urgencia:
        if palavra in texto.lower():
            indicadores["palavras_urgencia"].append(palavra)

    # 2. Detecção de pedidos de dinheiro
    if any(x in texto.lower() for x in ["pix", "transferência", "depósito", "dinheiro", "pagamento"]):
        indicadores["pede_dinheiro"] = True

    # 3. Detecção de links
    # Encontra qualquer URL que comece com http:// ou https://
    indicadores["links_encontrados"] = re.findall(r'https?://\S+', texto)

    # 4. Análise com IA
    # Nota: A IA será chamada mesmo se não houver indicadores técnicos, pois ela analisa o tom.
    resultado_ia = analisar_mensagem_com_ia(texto)

    return {
        "indicadores": indicadores,
        "analise_ia": resultado_ia
    }