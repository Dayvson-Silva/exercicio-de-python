

# função anonima lambda

quadrado = lambda x : x ** 2
print(quadrado(5))

par = lambda x : x % 2 == 0
print(par(10))

name_uppercase = lambda n : n.upper()
print(name_uppercase("euzinho"))

# ex 1
par_impar = lambda x :"par" if x % 2 == 0 else "impar"

print(par_impar(5))
print(par_impar(10))

# usando map 

num = [1,2,3,4,5]
quadrados = list(map(lambda x : x ** 2, num))
print(quadrados)

# usando reduce

from functools import reduce

numeros = [1,2,3,4,5]
soma = reduce(lambda x,y : x + y , numeros)
print(soma)

# usando filter

numeros = [1,2,3,4,5]
pares = list(filter(lambda x : x % 2 == 0 ,numeros))
print(pares)