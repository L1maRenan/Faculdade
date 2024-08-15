import random
lista = []
listapar = []
for i in range(21):
    numeros = random . randint(1, 101)
    lista.append(numeros)
for i in lista:
    if i % 2 == 0:
        listapar.append(i)
print(listapar)