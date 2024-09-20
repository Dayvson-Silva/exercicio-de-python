def adicao(numero1 , numero2):
    return numero1 + numero2

def subtracao(numero1 , numero2):
    return numero1 - numero2

def divisao(numero1 , numero2):
    return numero1 / numero2

def multiplicacao(numero1 , numero2):
     return numero1 * numero2

while True:


    print("\nEscolha uma das Operações Abaixo")

    print(" 1 - Adição \n 2 - Subtração \n 3 - Divisão \n 4 - Multiplicação \n 5 - Sair") 
    opcao= int(input("Opção Desejada :"))

    match opcao :
        case 1:
            numero1 = int(input("Digite um number:"))
            numero2 = int(input("Digite um number:"))

            print(adicao(numero1 , numero2))
        case 2:       
            numero1 = int(input("Digite um number:"))
            numero2 = int(input("Digite um number:"))

            print(subtracao(numero1 , numero2))
        case 3:
            numero1 = int(input("Digite um number:"))
            numero2 = int(input("Digite um number:"))

            if numero2 == 0:
                print("Seu fresco TE QUEBREI, APRENDA QUE NÃO PODE DIVIDIR POR 0!!!!!!!!!")
                break

            print(divisao(numero1 , numero2))

        case 4:
           

            numero1 = int(input("Digite um number:"))
            numero2 = int(input("Digite um number:"))

            print(multiplicacao(numero1 , numero2))
        case 5 :
            print("Calculadora the end!")
            break