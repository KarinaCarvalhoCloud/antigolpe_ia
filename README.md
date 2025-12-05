# 🛡️ AntiGolpe IA: Assistente de Detecção de Golpes e Phishing

## Visão Geral do Projeto

O **AntiGolpe IA** é um assistente de segurança pessoal desenvolvido para combater fraudes digitais comuns no Brasil. O projeto combina análise técnica de URLs com a capacidade de interpretação de linguagem natural de um modelo de Inteligência Artificial para detectar e explicar o risco em mensagens e links suspeitos.

É uma ferramenta essencial de conscientização e proteção, projetada para ser simples de usar por **pessoas reais** através de uma interface de linha de comando (CLI).

---

## 🚀 Funcionalidades Principais

| Módulo | Descrição | Tecnologias Chave |
| :--- | :--- | :--- |
| **1. Verificador de Links** | Analisa URLs em busca de IPs disfarçados, encurtadores e, crucialmente, **ataques de Homógrafos** (Punnycode, ex: `paypaI.com`). Calcula uma pontuação de risco. | Python, `requests`, `idna` |
| **2. Analisador de Mensagens IA** | Avalia o texto (ex: WhatsApp, SMS) em busca de sinais de Engenharia Social, como urgência, manipulação emocional e pedidos de dinheiro. | Python, OpenAI API (`gpt-4o-mini`) |
| **3. CLI (Interface)** | Menu interativo que unifica as ferramentas e fornece acesso ao Guia Anti-Golpe. | Python |
| **4. Guia Anti-Golpe** | Documentação didática sobre os golpes mais comuns no Brasil e checklist de segurança. | Markdown |

---

## ⚙️ Arquitetura e Estrutura

O projeto segue uma arquitetura modular, facilitando a manutenção e expansão.