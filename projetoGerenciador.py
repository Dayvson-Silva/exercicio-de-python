
while True:

    option = int(input("\n1 - Adicionar \n2 - Listar \n3 - Editar \n4 - Deletar \n5 - Sair \nDigite uma das opções listadas acima: "))

    match option:
        case 1:
            print("Você escolheu adicionar uma tarefa, siga os passos abaixo:")
            adicionar()
        
        case 2:
            print("Você escolheu listar uma tarefa, siga os passos abaixo:")
            listar()
        
        case 3:
            print("Você escolheu editar uma tarefa, siga os passos abaixo:")
            editar()
        
        case 4:
            print("Você escolheu deletar uma tarefa, siga os passos abaixo:")
            deletar()
        
        case 5:
            print("Você escolheu sair de tudo.")
            break