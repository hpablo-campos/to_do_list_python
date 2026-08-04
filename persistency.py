import pickle
from rich import print

def salvar_tarefas(tarefa, nome_arquivo='tarefas.pkl'):
    with open(nome_arquivo, 'wb') as arquivo:
        pickle.dump(tarefa, arquivo)
    print(f"[green3 b]-> Alteração salva em '{nome_arquivo}' com sucesso.\n[/]")

def carregar_tarefas(nome_arquivo='tarefas.pkl'):
    try:
        with open(nome_arquivo, 'rb') as arquivo:
            tarefa = pickle.load(arquivo)
            print(f"[green3 b]-> Arquivo '{nome_arquivo}' carregado com sucesso.\n[/]")
            return tarefa

    except FileNotFoundError:
        print(f"[bright_red b]-> Arquivo '{nome_arquivo}' não encontrado. Nenhuma tarefa foi carregada!\n[/]")
        return []

    except EOFError:
        print(f"[bright_red b]-> O arquivo '{nome_arquivo}' está vazio. Nenhuma tarefa foi carregada!\n[/]")
        return []