# 🤖 CrewAI Refactoring & Security Agent

Um agente autônomo de refatoração de código e mentoria técnica construído com **CrewAI** e **Ollama (Llama 3.2)**, projetado para rodar **100% localmente**. 

O objetivo deste projeto é analisar arquivos de código-fonte de forma dinâmica (suportando C, Python, JavaScript, Java, C#, etc.), identificar vulnerabilidades de segurança (ex: validações em Fetch APIs / HTTP), sugerir padrões de arquitetura (Design Patterns) e entregar a refatoração completa aplicada aos princípios de Clean Code e SOLID.

---

## 💡 Diferenciais do Projeto

- **Local-First & Privacy:** Toda a execução roda na sua máquina via Ollama. Nenhum código, chave de API ou dado sensível é enviado para a nuvem.
- **Entrada Dinâmica:** Pipeline flexível que aceita qualquer arquivo passado por parâmetro via linha de comando (`--inputs`).
- **Análise Dual (Security + Clean Code):** Diferencia automaticamente lógicas de negócio puro de código de integração (APIs/Fetch), aplicando boas práticas de tratamento de erros e parsing assíncrono.
- **Mentoria Técnica:** Além de reescrever o código, o agente fornece um resumo explicativo apontando *frameworks*, bibliotecas e melhorias estruturais recomendadas.

---

## 🛠️ Tecnologias Utilizadas

- **[CrewAI](https://crewai.com):** Framework para orquestração de agentes autônomos de IA.
- **[Ollama](https://ollama.com):** Execução local de LLMs.
- **Llama 3.2:** Modelo de linguagem local para análise e geração de código.
- **Python / PowerShell:** Ambiente de execução e automação CLI.

---

## 🚀 Como Executar

### Pré-requisitos

1. Possuir o **Python 3.10+** e o **CrewAI CLI** instalados.
2. Possuir o **Ollama** instalado e rodando com o modelo `llama3.2`:
   ```bash
   ollama pull llama3.2