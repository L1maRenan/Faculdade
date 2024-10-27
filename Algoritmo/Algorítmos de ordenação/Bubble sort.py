def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

import random
import time

listanumeros = []
for i in range(1, 1000000):
    numero = random.randint(1, 100)
    listanumeros.append(numero)

começo = time.time()
bubble_sort(listanumeros)
fim = time.time()

print(f"Tempo de organização pra o bubble sort: {fim-começo:.2f}")