from datetime import datetime

class Task:

    def __init__(self, titulo, descricao, data_vencimento, status = 'Pendente'):

        self.titulo = titulo
        self.descricao = descricao
        self.data_vencimento = datetime.strptime(data_vencimento, '%d/%m/%Y')
        self.status = status

    def __repr__(self):
        return (
            f"Tarefa(titulo = {self.titulo}, descricao = {self.descricao}, "
            f"data_vencimento = {self.data_vencimento.strftime('%d/%m/%Y')}, status = {self.status})"
        )

    def marcar_concluida(self):
        self.status = 'Concluída'

    def esta_atrasada(self):
        return datetime.now().date() > self.data_vencimento.date() and self.status == 'Pendente'

    def edit_titulo(self, novo_titulo):
        self.titulo = novo_titulo

    def edit_descricao(self, nova_descricao):
        self.descricao = nova_descricao

    def edit_data_venc(self, nova_data_venc):
        self.data_vencimento = datetime.strptime(nova_data_venc, "%d/%m/%Y")

    def detalhes(self):
        status = 'Atrasada' if self.esta_atrasada() else self.status
        return  (f'Título: {self.titulo}\n'
                 f'Descrição: {self.descricao}\n'
                 f'Status: {status}\n'
                 f'Data de Vencimento: {self.data_vencimento.strftime('%d/%m/%Y')}\n'
                 )