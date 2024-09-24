lista = []
def adicionarlista(nome, idade, cidade):
    cidadao = [f"Nome: {nome}, Idade: {idade}, Cidade {cidade}"]
    lista.append(cidadao)

adicionarlista("Renan", 18, "Saquarema")
adicionarlista("Fábio", 24, "Itauna")
adicionarlista("Felipe", 34, "Rio de Janeiro")
print(lista)