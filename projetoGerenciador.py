# Tarefas armazenadas
tarefas = [
    # {
    #     "nome": "caca",
    #     "Descrição": "cece",
    #     "prioridade": 1,
    #     "categoria": "coco",
    #     "Status": False,
    # },
    # {
    #     "nome": "kaka",
    #     "Descrição": "keke",
    #     "prioridade": 2,
    #     "categoria": "koko",
    #     "Status": False,
    # },
    # {
    #     "nome": "dada",
    #     "Descrição": "dede",
    #     "prioridade": 5,
    #     "categoria": "dodo",
    #     "Status": False,
    # },
]


# Função de adicionar tarefa
def add_tarefa():

    tarefa = {
        "Nome": input("Digite um nome para a tarefa: "),
        "Descrição": input("Digite a descrição da tarefa: "),
        "Prioridade": int(input("Digite a prioridade da tarefa usando 1 a 5: ")),
        "Categoria": input("Digite a categoria da tarefa: "),
        "Status": False,
    }
    tarefas.append(tarefa)
    print(tarefa)


# Função de listar tarefas
def listar_tarefas():

    prioridade = int(input("Escolha qual prioridade de tarefa voce deseja ver: "))

    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    for tarefa in range(len(tarefas)):

        prioridade_tarefa = tarefas[tarefa].get("Prioridade")

        if prioridade_tarefa == prioridade:
            for chave, valor in tarefas[tarefa].items():
                print(f"{chave}: {valor}")

        print()


# Função editar tarefa

while True:

    option = int(
        input(
            "\n1 - Adicionar \n2 - Listar \n3 - Editar \n4 - Deletar \n5 - Sair \nDigite uma das opções listadas acima: "
        )
    )

    match option:

        case 1:
            print("\nVocê escolheu adicionar uma tarefa, siga os passos abaixo:")
            add_tarefa()

        case 2:

            print("\nVocê escolheu listar tarefas, siga os passos abaixo \n")
            listar_tarefas()

        case 3:
            print("\nVocê escolheu editar uma tarefa, siga os passos abaixo:")
            editar()

        case 4:
            print("\nVocê escolheu deletar uma tarefa, siga os passos abaixo:")
            deletar()

        case 5:
            print("\nVocê escolheu sair de tudo.")
            break
