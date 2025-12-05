AntiGolpe IA — Assistente Inteligente de Prevenção a Golpes

O **AntiGolpe IA** é um projeto de Segurança + Inteligência Artificial criado para ajudar usuários comuns a identificarem possíveis golpes, mensagens suspeitas, links maliciosos e tentativas de engenharia social.

O sistema utiliza regras de segurança, análise contextual de texto e um modelo de IA para detectar sinais de fraude digital, como:
- phishing bancário  
- golpes do PIX  
- falsas atualizações de apps  
- mensagens de urgência  
- links maliciosos  

Este projeto foi desenvolvido com foco em educação digital e proteção de pessoas vulneráveis online.

---

## 🚀 Objetivos do Projeto

- Ajudar pessoas que não entendem de tecnologia a evitar golpes.
- Criar um sistema simples que analisa mensagens e diz se é suspeita.
- Utilizar IA e regras de segurança de forma transparente.
- Construir um portfólio profissional de Segurança e Inteligência Artificial.
- Evoluir para uma API e futuramente um app/aplicativo educativo.

---

## 📂 Estrutura do Repositório

antigolpe_ia/
│── analisador_ia.py # Código principal da análise de golpes
│── requirements.txt # Dependências do projeto
│── LICENSE # Licença MIT
│── README.md # Documentação do projeto
│── examples/ # Exemplos prontos para testar a ferramenta
│ ├── exemplo_1.txt
│ ├── exemplo_2.txt
│ └── exemplo_3.txt
│── security/ # Base de conhecimento de segurança
├── rules.json
├── url_blacklist.txt
└── phishing_signatures.txt

---

## 🧠 Como a análise funciona

A detecção utiliza várias camadas:

### ✔️ 1. **Regras de Segurança**
Via `security/rules.json`, contendo:
- padrões comuns de golpes
- termos de urgência
- ações perigosas
- domínios falsos

### ✔️ 2. **Assinaturas de phishing**
Frases comuns encontradas em golpes reais.

### ✔️ 3. **Lista negra de URLs**
`url_blacklist.txt` contém links maliciosos ou suspeitos.

### ✔️ 4. **Análise de IA**
Interpretação contextual da mensagem para identificar:
- manipulação emocional
- urgência artificial
- tentativa de extorquir dados
- engenharia social

---

## ▶️ Como Executar

### 1️⃣ Instale as dependências

No terminal:

```bash
pip install -r requirements.txt
2️⃣ Execute o analisador
bash
Copiar código
python analisador_ia.py
Você será solicitado a inserir uma mensagem ou URL.
A ferramenta dirá se é suspeita e por quê.

📌 Exemplos de Uso
Exemplo 1
arduino
Copiar código
"Seu banco bloqueou sua conta. Clique no link abaixo para liberar."
Saída esperada:


⚠️ Alerta: Essa mensagem contém forte indicação de phishing.
Motivos: urgência, pedido de clique, padrão de bloqueio falso.
Exemplo 2
arduino
Copiar código
"Oi mãe, troquei de número. Preciso que me faça um PIX urgente."
Saída:


⚠️ Possível golpe do falso familiar.
🧱 Próximas Funcionalidades
API REST com FastAPI

Integração com RAG (modelo usando PDFs reais de golpes)

Dashboard para análise

Classificador treinado com IA

Detecção de links automaticamente (regex + heurísticas)

Modo “educação digital” explicando cada golpe para leigos

🤝 Contribuições
Sinta-se livre para enviar:

melhorias de código

novas regras

links suspeitos

exemplos de golpes reais

sugestões de novas features

📄 Licença
Este projeto está licenciado sob a MIT License – veja o arquivo LICENSE para mais detalhes.

👩‍💻 Autora
Ana Karina
GenAI Engineer | CloudSecurity
GitHub: https://github.com/KarinaCarvalhoCloud
---

## ⚙️ Arquitetura e Estrutura


O projeto segue uma arquitetura modular, facilitando a manutenção e expansão.
