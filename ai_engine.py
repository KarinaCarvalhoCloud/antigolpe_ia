import openai

# 1. Configura o cliente da API (Novo Padrão)
# Substitua "SUA_API_KEY_AQUI" pela sua chave real.
CLIENTE_IA = openai.OpenAI(
    api_key="SUA_API_KEY_AQUI" 
)

def analisar_mensagem_com_ia(texto):
    """
    Usa a IA para avaliar o texto da mensagem e gerar uma análise detalhada.
    """
    prompt = f"""
Você é um Analista de Segurança especializado em golpes brasileiros.
Avalie a mensagem abaixo e responda no seguinte formato:

Risco: (0 a 100)
Por que pode ser golpe:
- ponto 1
- ponto 2
- ponto 3

Sinais comuns:
- item 1
- item 2

Resumo para leigos:
(explicar em linguagem simples)

Recomendação final:
(o que a pessoa deve fazer)

Mensagem recebida:
\"\"\"{texto}\"\"\"
    """

    try:
        # 2. Chamada atualizada para o modelo usando o objeto CLIENTE_IA
        resposta = CLIENTE_IA.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "Você é um especialista em segurança e detecção de phishing."},
                      {"role": "user", "content": prompt}]
        )

        # 3. Acessando o conteúdo da resposta na nova estrutura
        return resposta.choices[0].message.content
        
    except Exception as e:
        # Captura erros de autenticação ou conexão
        return f"Erro na comunicação com a API da OpenAI: {e}"