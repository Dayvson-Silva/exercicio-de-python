







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
        

