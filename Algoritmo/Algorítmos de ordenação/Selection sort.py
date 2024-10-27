def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
      
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
              
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

import random
import time

listanumeros = []
for i in range(1, 1000000):
    numero = random.randint(1, 100)
    listanumeros.append(numero)

começo = time.time()
selection_sort(listanumeros)
fim = time.time()

print(f"Tempo de organização pra o bubble sort: {fim-começo:.2f}")