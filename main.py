import argparse
from controller import Controller

def main():
    parser = argparse.ArgumentParser(description="Gerenciador de Tarefas CLI em Python")

    subparsers = parser.add_subparsers(dest="comando", help="comandos disponíveis")

    # Adicionar nova tarefa
    parser_adicionar = subparsers.add_parser("adicionar", help="Adicionar nova tarefa")
    parser_adicionar.add_argument("titulo", type=str, help="Título da tarefa")
    parser_adicionar.add_argument("descricao", type=str, help="Descrição da tarefa")
    parser_adicionar.add_argument("data_vencimento", type=str, help="Data de vencimento da tarefa no formato 'dd/mm/aaaa'")

    # Listar tarefas
    parser_listar = subparsers.add_parser("listar", help="Listar todas as tarefas")
    parser_listar.add_argument("--status", choices=["Pendente", "Concluída"], help="Filtrar por 'status' da tarefa")

    # Editar tarefas
    parser_editar = subparsers.add_parser("editar", help="Editar uma tarefa")
    parser_editar.add_argument("indice", type=int, help="Índice da tarefa a ser editada")
    parser_editar.add_argument("--titulo", type=str, help="Novo título da tarefa")
    parser_editar.add_argument("--descricao", type=str, help="Nova descrição da tarefa")
    parser_editar.add_argument("--data_vencimento", type=str, help="Nova data de vencimento da tarefa no formato 'dd/mm/aaaa'")

    # Remover tarefas
    parser_remover = subparsers.add_parser("remover", help="Remover uma tarefa")
    parser_remover.add_argument("indice", type=int, help="Índice da tarefa a ser removida")

    # Concluir tarefas
    parser_concluir = subparsers.add_parser("concluir", help="Marca uma tarefa como concluída")
    parser_concluir.add_argument("indice", type=int, help="Índice da tarefa concluída")

    # Processar argumentos

    args = parser.parse_args()
    gerenciador = Controller()

    comandos = {
        "adicionar":    lambda: gerenciador.add_tarefa(args.titulo, args.descricao, args.data_vencimento),
        "listar":       lambda: gerenciador.listar_tarefas(args.status),
        "editar":       lambda: gerenciador.editar_tarefa(args.indice - 1, args.titulo, args.descricao, args.data_vencimento),
        "remover":      lambda: gerenciador.remover_tarefa(args.indice - 1),
        "concluir":     lambda: gerenciador.marcar_concluida(args.indice - 1)
    }

    action = comandos.get(args.comando)
    if action:
        action()

    else:
        parser.print_help()
    
if __name__ == "__main__":
    main()