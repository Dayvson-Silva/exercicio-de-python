



# resultado vem com dicionario

def mostrar_info(**coisa):
    for chave,valor in coisa.items():
        print(f"{chave}: {valor}")


mostrar_info(nome="eu", idade=30,cidade="borel")



