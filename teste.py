tarefas = [
    {
        "Nome": "passear",
        "Descrição": "sair com o cachorro",
        "Prioridade": 2,
        "Categoria": "diversao",
        "Status": False,
    },
    {
        "Nome": "jogar",
        "Descrição": "jogar bola",
        "Prioridade": 1,
        "Categoria": "diversao",
        "Status": False,
    },
]

editar = int(input("Digite a tarefa que deseja editar: "))
editar_tarefa = tarefas[editar]
print(editar_tarefa)
