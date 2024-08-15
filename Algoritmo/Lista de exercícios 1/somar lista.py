import random
lista = []
for i in range(21):
    numeros = random.randint(1, 101)
    lista.append(numeros)

print(lista)
soma = sum(lista)
print(f"A soma dos numeros desta lista é igual a {soma}")