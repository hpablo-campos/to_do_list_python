import pickle

def salvar_tarefas(tarefa, nome_arquivo='tarefas.pkl'):
    with open(nome_arquivo, 'wb') as arquivo:
        pickle.dump(tarefa, arquivo)

def carregar_tarefas(nome_arquivo='tarefas.pkl'):
    try:
        with open(nome_arquivo, 'rb') as arquivo:
            tarefa = pickle.load(arquivo)
            print(f"Tarefas carregadas de '{nome_arquivo}'com sucesso!")
            return tarefa

    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado. Nenhuma tarefa foi carregada!")
        return []

    except EOFError:
        print(f'O arquivo {nome_arquivo} está vazio. Nenhuma tarefa foi carregada!')
        return []