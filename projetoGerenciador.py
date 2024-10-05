# Tarefas armazenadas
tarefas = []

# Função de adicionar tarefa
def add_tarefa():

    tarefa = {
        "Nome": input("\033[1mDigite um nome para a tarefa:\033[m "),
        "Descrição": input("\033[1mDigite a descrição da tarefa:\033[m "),
        "Prioridade": int(input("\033[1mDigite a prioridade da tarefa usando 1 a 5:\033[m ")),
        "Categoria": input("\033[1mDigite a categoria da tarefa:\033[m "),
        "Status": False,
    }
    tarefas.append(tarefa)
    print(tarefa)

# Função de listar tarefas
def listar_tarefas():
    listar = int(input("\033[1m1 - Todas as tarefas de forma ordenada \n2 - Apenas por prioridade\033[m \nDigite como você quer listar as tarefas: "))
    match listar:
        case 1:
            print("\nVocê escolheu listar \033[1mtodas as tarefas de forma ordenada\033[m")

            # Contador de tarefas
            contador_tarefa = 1

            # Verifica se há alguma tarefa na lista
            if not tarefas:
                print("\033[1;31mNenhuma tarefa encontrada.\033[m")
                return
            
            for tarefa in tarefas:  
                print(f"\n\033[1m-------------------- Tarefa {contador_tarefa} ------------------------\033[m")

                # Pega a chave e o valor da tarefa atual pelo índice da tarefa atual
                for chave, valor in tarefas[tarefas.index(tarefa)].items():
                    print(f"{chave}: {valor}")
                
                contador_tarefa += 1
                
                # Espaço final pra cada tarefa
                print("\033[1m------------------------------------------------------\033[m")
            
        case 2:
            print("\nVocê escolheu listar por \033[1mprioridade\033[m")
            prioridade = int(input("Escolha qual prioridade de tarefa voce deseja ver: "))

            # Contador de tarefas
            contador_tarefa = 1

            # Verifica se há alguma tarefa na lista
            if not tarefas:
                print("\033[1;31mNenhuma tarefa encontrada.\033[m")
                return
            
            # Para a tarefa atual no range do tamanho da lista de tarefas
            for tarefa in range(len(tarefas)):
                # Pega o valor da chave "Prioridade"
                prioridade_tarefa = tarefas[tarefa].get("Prioridade")

                # Verifica se o valor da chave "Prioriadade" atual é igual ao valor que o úsuario digitou anteriormente
                if prioridade_tarefa == prioridade:
                    print(f"\n\033[1m-------------------- Tarefa {contador_tarefa} ------------------------\033[m")
                    
                    # Pega a chave e o valor da chave atual e transforma a lista em dicionário para printar
                    for chave, valor in tarefas[tarefa].items():
                        print(f"{chave}: {valor}")

                contador_tarefa += 1

                # Espaço final pra cada tarefa
                print("\033[1m------------------------------------------------------\033[m")

# Função editar tarefa
def editar_tarefa():
    # Para a tarefa autal no range do tamanho da lista de tarefas
    for tarefa in range(len(tarefas)):

        # Printa a chave e o valor da tarefa atual
        for chave, valor in tarefas[tarefa].items():
            print(f"{chave}: {valor}")

        # Espaço em branco
        print()
    
    # Verifica se tem tarefa
    if not tarefas:
        print("\033[1;31mNenhuma tarefa encontrada.\033[m")
        return
    
    editar = int(input("Qual tarefa você deseja editar(Obs.: 1 - primeira, 2 - segunda, ...): "))
    print()

    # Armazena qual tarefa o usuario quer editar
    tarefa_escolhida = tarefas[editar - 1]

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

    # Pega o nome da tarefa que o usuario deseja deletar
    nome_tarefa = input("Digite o nome da tarefa que deseja \033[1;31mdeletar\033[m: ")

    for tarefa in tarefas:
        
        
        if tarefa['Nome'] == nome_tarefa:

            tarefas.remove(tarefa)
            print(f'\033[1mTarefa "{nome_tarefa}" deletada.\033[m')
            return
        
    print(f'Tarefa "{nome_tarefa}" não encontrada.')

# Função concluir tarefas
def concluir_tarefa():
    nome_tarefa = input("Digite o nome da tarefa que deseja concluir: ")
    for tarefa in tarefas:
        if tarefa['Nome'] == nome_tarefa:
            tarefa['Status'] = True
            print(f'Tarefa "{nome_tarefa}" concluída.')
            return
        print(f'Tarefa "{nome_tarefa}" não encontrada.')
        
while True:

    print("\n\033[1;32m====================- Gerenciador de tarefas -====================\033[m")
    option = int(
        input(
            "\n\033[1m1 - Adicionar \n2 - Listar \n3 - Editar \n4 - Deletar \n5 - Concluir \n6 - Sair \nDigite uma das opções listadas acima:\033[m "
        )
    )

    match option:

        case 1:
            print("\n\033[1;32m===========================- Adicionar -===========================\033[m")
            print("\033[1mVocê escolheu adicionar uma tarefa, siga os passos abaixo\033[m\n")
            add_tarefa()

        case 2:

            print("\n\033[1;32m===========================- Listar -===========================\033[m")
            print("\033[1mVocê escolheu listar tarefas, siga os passos abaixo\033[m\n")
            listar_tarefas()

        case 3:
            print("\n\033[1;32m===========================- Editar -===========================\033[m")
            print("\033[1mVocê escolheu editar uma tarefa, siga os passos abaixo\033[m\n")
            editar_tarefa()

        case 4:
            print("\n\033[1;32m===========================- Deletar -===========================\033[m")
            print("\033[1mVocê escolheu deletar uma tarefa, siga os passos abaixo\033[m\n")
            deletar_tarefa()

        case 5:
            print("\n\033[1;32m===========================- Concluir -===========================\033[m")
            print("\033[1mVocê escolheu concluir uma tarefa, siga os passos abaixo\033[m\n")
            concluir_tarefa()

        case 6:
            print("\nVocê escolheu sair de tudo.")
            break