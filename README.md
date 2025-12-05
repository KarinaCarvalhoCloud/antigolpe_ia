# AntiGolpe IA — Assistente Inteligente de Prevenção a Golpes

O **AntiGolpe IA** é um projeto de Segurança + Inteligência Artificial criado para ajudar usuários comuns a identificarem possíveis golpes, mensagens suspeitas, links maliciosos e tentativas de engenharia social. O sistema utiliza regras de segurança, análise contextual de texto e um modelo de IA para detectar sinais de fraude digital, como:

- phishing bancário
- golpes do PIX
- falsas atualizações de apps
- mensagens de urgência
- links maliciosos

Este projeto foi desenvolvido com foco em educação digital e proteção de pessoas vulneráveis online.

## 🚀 Objetivos do Projeto
- Ajudar pessoas que não entendem de tecnologia a evitar golpes.
- Criar um sistema simples que analisa mensagens e diz se é suspeita.
- Utilizar IA e regras de segurança de forma transparente.
- Construir um portfólio profissional de Segurança e Inteligência Artificial.
- Evoluir para uma API e futuramente um app/aplicativo educativo.


## 🧠 Como a análise funciona
A detecção utiliza várias camadas:

### ✔️ 1. Regras de Segurança
Via `security/rules.json`, contendo:

- padrões comuns de golpes
- termos de urgência
- ações perigosas
- domínios falsos

### ✔️ 2. Assinaturas de phishing
Frases comuns encontradas em golpes reais.

### ✔️ 3. Lista negra de URLs
`url_blacklist.txt` contém links maliciosos ou suspeitos.

### ✔️ 4. Análise de IA
Interpretação contextual da mensagem para identificar:

- manipulação emocional
- urgência artificial
- tentativa de extorquir dados
- engenharia social

## ▶️ Como Executar
### 1️⃣ Instale as dependências
No terminal:

bash
pip install -r requirements.txt


### 2️⃣ Execute o analisador

bash
python analisador_ia.py

Você será solicitado a inserir uma mensagem ou URL. A ferramenta dirá se é suspeita e por quê.

## 📌 Exemplos de Uso
### Exemplo 1
*Entrada:* "Seu banco bloqueou sua conta. Clique no link abaixo para liberar."

Saída esperada: ⚠️ Alerta: Essa mensagem contém forte indicação de phishing. Motivos: urgência, pedido de clique, padrão de bloqueio falso.

### Exemplo 2
*Entrada:* "Oi mãe, troquei de número. Preciso que me faça um PIX urgente."

*Saída:* "Possível golpe do falso familiar."

## 🧱 Próximas Funcionalidades
- *API REST com FastAPI:* Permitir que outras aplicações e serviços consumam a lógica de análise de golpes como um serviço web.
- *Integração com RAG (Retrieval-Augmented Generation):* Utilizar um modelo de linguagem (LLM) que consulta uma base de dados externa (seus PDFs reais de golpes) para gerar respostas mais informadas e contextuais.
- *Dashboard para análise:* Criar uma interface gráfica para visualizar estatísticas de uso, tipos de golpes mais detectados e tendências.
- *Classificador treinado com IA:* Desenvolver um modelo de _machine learning_ customizado (em vez de usar uma API externa) para classificar o risco da mensagem.
- *Detecção de links automaticamente:* Implementar o uso de *regex* (expressões regulares) e *heurísticas* avançadas para extrair e analisar URLs presentes no corpo da mensagem.
- *Modo “educação digital”:* Adicionar uma funcionalidade que, ao detectar um golpe, explique o mecanismo da fraude (engenharia social, gatilhos) em *linguagem simples para leigos*.

## 🤝 Contribuições
Sinta-se livre para enviar:

- melhorias de código
- novas regras
- links suspeitos
- exemplos de golpes reais
- sugestões de novas features

## 📄 Licença
Este projeto está licenciado sob a *MIT License* – veja o arquivo `LICENSE` para mais detalhes.

## 👩‍💻 Autora
**Ana Karina**
GenAI Engineer | CloudSecurity
GitHub: https://github.com/KarinaCarvalhoCloud
## ⚌️ Arquitetura e Estrutura
O projeto segue uma arquitetura modular, facilitando a manutenção e expansão.

```

