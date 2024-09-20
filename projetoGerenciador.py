




tarefas = []

def add_tarefa():
    
    tarefa ={
        "nome": input("Digite um nome para a tarefa: "),
        "Descrição": input("Digite a descrição da tarefa: "),
        "prioridade": input("Digite a prioridade da tarefa: "),
        "categoria":  input("Digite a categoria da tarefa: "),
        "Status": False
    }
    tarefas.append(tarefa)

def listar_tarefas():
    



    while True:
        print("digite 1")
        op = int(input("digite a opção:"))
        if op == 1:
            add_tarefa()
    
      
       
       



