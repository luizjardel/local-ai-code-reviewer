# 🤖 Local-First AI Refactoring Agent

Um agente de inteligência artificial local e autónomo, desenvolvido com **CrewAI**, **Ollama (Llama 3.2)** e automação em **PowerShell**, focado em análise de código estático, aplicação de princípios **Clean Code**, **SOLID** e auditoria de segurança para portfólios profissionais.

---

## 🚀 Sobre o Projeto

Este projeto foi concebido para atuar como um revisor e refatorador de código automatizado diretamente no ambiente local do desenvolvedor. A ferramenta analisa ficheiros de código-fonte (suporte a múltiplas linguagens como Python, C, Java, JavaScript, etc.), identifica pontos de melhoria estrutural, vulnerabilidades e gargalos de desempenho, gerando relatórios detalhados e códigos refatorados prontos para produção.

---

## 🛠️ Tecnologias Utilizadas

* **Orquestração de IA:** [CrewAI](https://www.crewai.com/)
* **Modelos Locais (LLM):** [Ollama](https://ollama.com/) (Llama 3.2)
* **Ambiente de Execução:** Python, PowerShell / Bash
* **Controle de Versão:** Git & GitHub

---

## 📂 Estrutura do Repositório

```text
├── agents/             # Definições estruturais dos agentes de IA
├── knowledge/          # Bases de conhecimento e preferências de contexto
├── tools/              # Ferramentas modulares customizadas
├── test.py             # Ficheiro de exemplo para testes em Python
├── teste.c             # Ficheiro de exemplo para testes em C
├── crew.jsonc          # Configuração central das tarefas e do fluxo (Crew)
├── CREWAI_DOCS.md      # Documentação de referência interna do CrewAI
└── README.md           # Documentação principal do projeto