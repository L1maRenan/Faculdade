def fibonacci(n):
    sequencia = [0, 1]
    for i in range(2, n):
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)
    return sequencia

n = 10  
resultado = fibonacci(n)
print(resultado)

