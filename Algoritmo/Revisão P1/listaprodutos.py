produtos = {
    "Arroz": 10,
    "Feijão": 5,
    "Macarrão": 8,
    "Azeite": 2,
    "Açúcar": 6,
    "Café": 3,
    "Leite": 12,
    "Farinha": 7
}
def consultar(produto):
    encontrado = False
    for a, b in produtos.items():
        if produto == a:
            encontrado = True
            print(f"Produto: {produto}\nUnidades disponíveis:{b}")
            break
    if encontrado == False:
        print(f"Tem {produto} aqui não man")

consultar("Abacate")
