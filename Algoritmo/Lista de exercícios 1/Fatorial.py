numero = int(input("Digite um número: "))
n = numero

def fatorial(n):
    resultado = 1
    while n > 0:
        resultado *= n
        n -= 1
    return resultado

print(f"O fatorial de {numero} é {fatorial(numero)}")
