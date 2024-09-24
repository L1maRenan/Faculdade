produtos = {
    "Arroz": 20.00,
    "Feijão": 8.50,
    "Macarrão": 9.20,
    "Azeite": 48.99,
    "Açúcar": 5.89,
    "Café": 17.99,
    "Leite": 5.69,
    "Farinha": 2.99
}

def maiscaro(dicionario):
    for i, b in dicionario.items():
        if b == max(dicionario.values()):
            return (f"{i}: {b}")

result = maiscaro(produtos)
print(result)