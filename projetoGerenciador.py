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
def editar_tarefa():
    # Para a tarefa autal no range do tamanha da lista de tarefas
    for tarefa in range(len(tarefas)):

        # Printa a chave e o valor da tarefa atual
        for chave, valor in tarefas[tarefa].items():
            print(f"{chave}: {valor}")

        # Espaço em branco
        print()

    editar = int(input("DIGITE O ÍNDICE DA TAREFA QUE VOCÊ DESEJA EDITAR: "))

    # Armazena qual tarefa o usuario quer editar
    tarefa_escolhida = tarefas[editar]

    # Itera sobre as chaves e valores da tarefa escolhida
    for _ in tarefa_escolhida:
        # Armazena o que o usuario quer editar na tarefa
        campo = int(
            input(
                "\n1 - Editar nome \n2 - Editar descrição \n3 - Editar prioridade \n4 - Editar categoria \n5 - voltar \nEscolha qual campo você deseja editar: "
            )
        )

        match campo:
            case 1:
                print("\nVocê escolheu editar nome, siga os passos abaixo")
                campo_nome = tarefa_escolhida.get("Nome")
                mudar_nome = str(
                    input(
                        f"\nDigite o nome que você quer que seja no lugar de {campo_nome}: "
                    )
                )
                # Muda o valor da chave escolhida(nome)
                tarefa_escolhida["Nome"] = mudar_nome

            case 2:
                print("\nVocê escolheu editar descrição, siga os passos abaixo")
                campo_desc = tarefa_escolhida.get("Descrição")
                mudar_desc = str(
                    input(
                        f"\nDigite a descrição que você quer que seja no lugar de {campo_desc}: "
                    )
                )
                # Muda o valor da chave escolhida(descrição)
                tarefa_escolhida["Descrição"] = mudar_desc

            case 3:
                print("\nVocê escolheu editar prioridade, siga os passos abaixo")
                campo_prioridade = tarefa_escolhida.get("Prioridade")
                mudar_prioridade = str(
                    input(
                        f"\nDigite a descrição que você quer que seja no lugar de {campo_prioridade}: "
                    )
                )
                # Muda o valor da chave escolhida(prioridade)
                tarefa_escolhida["Prioridade"] = mudar_prioridade

            case 4:
                print("\nVocê escolheu editar categoria, siga os passos abaixo")
                campo_categoria = tarefa_escolhida.get("Categoria")
                mudar_categoria = str(
                    input(
                        f"\nDigite o categoria que você quer que seja no lugar de {campo_categoria}: "
                    )
                )
                # Muda o valor da chave escolhida(categoria)
                tarefa_escolhida["Categoria"] = mudar_categoria

            case 5:
                # Volta pra qual tarefa o usuario deseja editar
                editar_tarefa()

   
# Função deletar tarefa
def deletar_tarefa():
    nome_tarefa = input("Digite o nome da tarefa que deseja deletar: ")
    for tarefa in tarefas:
        if tarefa['Nome'] == nome_tarefa:
            tarefas.remove(tarefa)
            print(f'Tarefa "{nome_tarefa}" deletada.')
            return
    print(f'Tarefa "{nome_tarefa}" não encontrada.')







tarefas = []

def add_tarefa():
    
    tarefa ={
        "nome": input("Digite um nome para a tarefa: "),
        "Descrição": input("Digite a descrição da tarefa: "),
        "prioridade": int(input("Digite a prioridade da tarefa usando 1 a 5: ")),
        "categoria":  input("Digite a categoria da tarefa: "),
        "Status": False
    }
    tarefas.append(tarefa)
    

def listar_tarefas():
    prioridade = int(input("Digite a prioridade da sua tarefa :"))
    if  prioridade == 1:
        print("Prioridade Extrema")
    elif prioridade == 2:
        print("prioridade maxima")
    elif prioridade == 3:
        print("Prioridade Alta")
    elif prioridade == 4:
        print("Prioridade Média")
    elif prioridade == 5:
        print("Prioridade Baixa")
    else:
        print("DESSA VEZ NÃO PAPAI")
        
    
    print(tarefas)

      
       
while True:
<<<<<<< HEAD

    option = int(input("\n1 - Adicionar \n2 - Listar \n3 - Editar \n4 - Deletar \n5 - Sair \nDigite uma das opções listadas acima: "))

    match option:

        case 1:
            print("\nVocê escolheu adicionar uma tarefa, siga os passos abaixo:")
            add_tarefa()
        
        case 2:
            
            print(tarefas)
            print("\nVocê escolheu listar uma tarefa, siga os passos abaixo:")
            listar_tarefas()
        
        case 3:
            print("\nVocê escolheu editar uma tarefa, siga os passos abaixo:")
            editar()
        
        case 4:
            print("Você escolheu deletar uma tarefa, siga os passos abaixo:")
            deletar()
        
        case 5:
            print("Você escolheu sair de tudo.")
            break
        
=======
>>>>>>> feat/menu

    print("\n====================- Gerenciador de tarefas -====================")
    option = int(
        input(
            "\n1 - Adicionar \n2 - Listar \n3 - Editar \n4 - Deletar \n5 - Concluir \n6 - Sair \nDigite uma das opções listadas acima: "
        )
    )

    match option:

        case 1:
            print("\n====================- Adicionar -====================")
            print("Você escolheu adicionar uma tarefa, siga os passos abaixo\n")
            add_tarefa()

        case 2:

            print("\n====================- Listar -====================")
            print("Você escolheu listar tarefas, siga os passos abaixo\n")
            listar_tarefas()

        case 3:
            print("\n====================- Editar -====================")
            print("Você escolheu editar uma tarefa, siga os passos abaixo\n")
            editar_tarefa()

        case 4:
            print("\n====================- Deletar -====================")
            print("Você escolheu deletar uma tarefa, siga os passos abaixo\n")
            deletar_tarefa()

        case 5:
            print("\n====================- Concluir -====================")
            print("Você escolheu concluir uma tarefa, siga os passos abaixo\n")
            concluir()

        case 6:
            print("\nVocê escolheu sair de tudo.")
            break
