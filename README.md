# 📝 CLI Task Manager (Gerenciador de Tarefas via Terminal)

Um gerenciador de tarefas simples, eficiente e modular em linha de comando (CLI), desenvolvido em Python. O sistema permite criar, listar, editar, concluir e remover tarefas com suporte a persistência local de dados e verificação automática de tarefas atrasadas.

---

## 🚀 Funcionalidades

- ➕ **Adicionar Tarefas:** Criação de tarefas com título, descrição e data de vencimento.
- 📋 **Listar Tarefas:** Visualização de todas as tarefas cadastradas com filtragem opcional por status (`Pendente` / `Concluída`).
- ⏰ **Detecção de Atraso:** Identificação e exibição automática do status `Atrasada` caso a data atual ultrapasse a data de vencimento.
- ✏️ **Editar Tarefas:** Atualização flexível de título, descrição e/ou data de vencimento.
- ✅ **Concluir Tarefas:** Alteração de status de tarefas pendentes para concluídas.
- 🗑️ **Remover Tarefas:** Exclusão de tarefas a partir do seu índice.
- 💾 **Persistência de Dados:** Salvamento e carregamento automático das tarefas em arquivo local via módulo `pickle` (`tarefas.pkl` gerado automaticamente).

---

## 📁 Estrutura do Projeto

O projeto adota uma arquitetura modular orientada a objetos (MVC simplificado):

```
.
├── task.py          # Classe Task (modelo de dados e regras de negócio)
├── persistency.py   # Funções de leitura/escrita em arquivo (pickle)
├── controller.py    # Classe Controller (gerenciamento e fluxo de dados)
└── main.py          # Interface CLI principal (parser de argumentos com argparse)
```

---

## 🛠️ Pré-requisitos

- **Python 3.7+** instalado na sua máquina.
- Nenhuma biblioteca externa é necessária (utiliza apenas a biblioteca padrão do Python).

---

## ⚙️ Instalação e Execução

1. **Clone ou baixe o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/gerenciador-de-tarefas-cli.git
   cd gerenciador-de-tarefas-cli
   ```

2. **Execute os comandos através do `main.py`:**
   ```bash
   python main.py --help
   ```

---

## 📖 Como Usar (Guia de Comandos)

### 1. Adicionar uma nova tarefa
Sintaxe: `python main.py adicionar "<titulo>" "<descricao>" "<dd/mm/aaaa>"`

```bash
python main.py adicionar "Estudar Python" "Revisar POO e Argparse" "15/08/2026"
```

### 2. Listar tarefas
Sintaxe: `python main.py listar [--status <Pendente|Concluída>]`

- Listar **todas** as tarefas:
  ```bash
  python main.py listar
  ```

- Filtrar apenas tarefas **pendentes**:
  ```bash
  python main.py listar --status Pendente
  ```

- Filtrar apenas tarefas **concluídas**:
  ```bash
  python main.py listar --status Concluída
  ```

### 3. Concluir uma tarefa
Sintaxe: `python main.py concluir <indice_da_tarefa>` *(Nota: o índice começa em 1)*

```bash
python main.py concluir 1
```

### 4. Editar uma tarefa
Sintaxe: `python main.py editar <indice_da_tarefa> [--titulo <novo_titulo>] [--descricao <nova_descricao>] [--data_vencimento <dd/mm/aaaa>]`

- Editar apenas o título:
  ```bash
  python main.py editar 1 --titulo "Estudar Python Avançado"
  ```

- Editar descrição e data de vencimento:
  ```bash
  python main.py editar 1 --descricao "Aprofundar em Decoradores e Geradores" --data_vencimento "20/08/2026"
  ```

### 5. Remover uma tarefa
Sintaxe: `python main.py remover <indice_da_tarefa>`

```bash
python main.py remover 1
```

---

## 📊 Exemplo de Saída no Terminal

```text
TAREFA 1:
Título: Estudar Python
Descrição: Revisar POO e Argparse
Status: Pendente
Data de Vencimento: 15/08/2026

Fim da lista de tarefas.
```

---

## 📄 Licença

Este projeto é livre para uso educacional e de estudo (MIT License).
