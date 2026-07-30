from task import Task
from persistency import salvar_tarefas, carregar_tarefas

class Controller:

    def __init__(self, nome_arquivo='tarefas.pkl'):
        self.nome_arquivo = nome_arquivo
        self.tarefas = carregar_tarefas(nome_arquivo)

    def add_tarefa(self, titulo, descricao, data_vencimento):
        nova_tarefa = Task(titulo, descricao, data_vencimento)
        self.tarefas.append(nova_tarefa)
        print(f"-> Tarefa '{titulo}' adicionada com sucesso.\n")
        self.salvar()

    def listar_tarefas(self, status=None):
        if not self.tarefas:
            print("-> Nenhuma tarefa encontrada!\n")
            return

        for i, tarefa in enumerate(self.tarefas):
            if status is None or tarefa.status == status:
                print(f'\nTAREFA {i + 1}:\n{tarefa.detalhes()}')
        print("\nFim da lista de tarefas.\n")

    def editar_tarefa(self, indice, titulo=None, descricao=None, data_vencimento=None):
        if 0 <= indice < len(self.tarefas):
            tarefa = self.tarefas[indice]
            if titulo:
                tarefa.edit_titulo(titulo)

            if descricao:
                tarefa.edit_descricao(descricao)

            if data_vencimento:
                tarefa.edit_data_venc(data_vencimento)

            print(f'-> Tarefa {indice + 1} editada com sucesso!\n')
            self.salvar()

        else:
            print(f"-> Índice inválido!\n")

    def remover_tarefa(self, indice):
         if 0 <= indice < len(self.tarefas):
            self.tarefas.pop(indice)
            print(f"-> Tarefa {indice + 1} foi removida com sucesso.\n")
            self.salvar()

         else:
            print(f"-> Índice inválido!\n")

    def marcar_concluida(self, indice):
        if 0 <= indice < len(self.tarefas):
            tarefa = self.tarefas[indice]
            tarefa.marcar_concluida()
            print(f"-> Tarefa {indice + 1} marcada como concluída.")
            self.salvar()

        else:
            print(f"-> Índice inválido!\n")
    
    def salvar(self):
        salvar_tarefas(self.tarefas, self.nome_arquivo)

