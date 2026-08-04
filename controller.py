from task import Task
from persistency import salvar_tarefas, carregar_tarefas
from rich.console import Console


console = Console()

class Controller:

    def __init__(self, nome_arquivo='tarefas.pkl'):
        self.nome_arquivo = nome_arquivo
        self.tarefas = carregar_tarefas(nome_arquivo)

    def add_tarefa(self, titulo, descricao, data_vencimento):
        nova_tarefa = Task(titulo, descricao, data_vencimento)
        self.tarefas.append(nova_tarefa)
     
        console.print(f"[green3 b]-> Tarefa [u]'{titulo}'[/u] adicionada com sucesso.\n[/]")
        self.salvar()

    def listar_tarefas(self, status=None):
        if not self.tarefas:
            console.print("[bright_red b]-> Nenhuma tarefa encontrada!\n[/]")
            return

        for i, tarefa in enumerate(self.tarefas):
            if status is None or tarefa.status == status:
                console.print(f"\n[cyan b]TAREFA {i + 1}:[/]")
                
                console.print(tarefa.detalhes())
                
        console.print("[dim]\nFim da lista de tarefas.\n[/]")

    def editar_tarefa(self, indice, titulo=None, descricao=None, data_vencimento=None):
        if 0 <= indice < len(self.tarefas):
            tarefa = self.tarefas[indice]
            if titulo:
                tarefa.edit_titulo(titulo)

            if descricao:
                tarefa.edit_descricao(descricao)

            if data_vencimento:
                tarefa.edit_data_venc(data_vencimento)

            console.print(f"[green3 b]-> Tarefa {indice + 1} editada com sucesso!\n[/]")
            self.salvar()
        else:
            console.print("[bright_red b]-> Índice inválido!\n[/]")

    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas.pop(indice)
            console.print(f"[green3 b]-> Tarefa {indice + 1} foi removida com sucesso.\n[/]")
            self.salvar()
        else:
            console.print("[bright_red b]-> Índice inválido!\n[/]")

    def marcar_concluida(self, indice):
        if 0 <= indice < len(self.tarefas):
            tarefa = self.tarefas[indice]
            tarefa.marcar_concluida()
            console.print(f"[green3 b]-> Tarefa {indice + 1} marcada como concluída.\n[/]")
            self.salvar()
        else:
            console.print("[bright_red b]-> Índice inválido!\n[/]")
    
    def salvar(self):
        salvar_tarefas(self.tarefas, self.nome_arquivo)