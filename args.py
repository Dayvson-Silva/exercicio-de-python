

# o resultado vem como tupla

def somar_numeros(*bola):
    resultado=0
    for num in bola:
        resultado += num
    return resultado

print(somar_numeros(1,2,3))
print(somar_numeros(10,20,30))
