from task import Task
from persistency import salvar_tarefas, carregar_tarefas

task1 = Task('Estudar Python', 'Estudar libs padrão do Python', '26/07/2026')
print(task1)

salvar_tarefas([task1])
tasks = carregar_tarefas()

print(tasks[0].detalhes())