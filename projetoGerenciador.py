# Tarefas armazenadas
tarefas = []


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

    # Verifica se há alguma tarefa na lista
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    # Para a tarefa atual no range do tamanho da lista de tarefas
    for tarefa in range(len(tarefas)):

        # Pega o valor da chave "Prioridade"
        prioridade_tarefa = tarefas[tarefa].get("Prioridade")

        # Verifica se o valor da chave "Prioriadade" atual é igual ao valor que o úsuario digitou anteriormente
        if prioridade_tarefa == prioridade:

            # Pega a chave e o valor da chave atual e transforma a lista em dicionário para printar certinho
            for chave, valor in tarefas[tarefa].items():
                print(f"{chave}: {valor}")

        # Espaço em branco pra cada tarefa
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
