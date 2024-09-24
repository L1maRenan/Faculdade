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

def produtosestoque(dic, produto, vendas):
    for a, b in dic.items():
        if a == produto:
            novoestoque = b - vendas
            if novoestoque < 0:
                return "Aquantidade vendida execede o estoque." 
            dic[produto] = novoestoque
    return dic

a = produtosestoque(produtos, "Arroz", 11)
print(a)