def concatenar_strings(*args):
    resultado = " " 
    for juntar in args:
        resultado += juntar
    return resultado
       
while True:




    nome =  input("digite 1 :")
    nome1 = input("digite 2 :")

   
    print(concatenar_strings(nome,nome1))

