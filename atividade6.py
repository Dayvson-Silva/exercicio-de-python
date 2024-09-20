

from functools import reduce

print("Digite 4 nomes o maior nome serar printado na tela")

nome = input("Digite o primeiro  nome :")
nome1 = input("Digite o  segundo nome :")
nome2 = input("Digite o terceiro  nome :")
nome3 = input("Digite o quarto  nome :")


nomes = [nome,nome1,nome2,nome3]
soma = reduce(lambda x,y : x  if len(x ) > len(y) else y ,nomes)
print(soma)
