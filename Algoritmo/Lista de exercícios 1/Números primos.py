numero = int(input("DIgite um número:"))
m = 100
lista = []
def primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if primo(numero) == True:
    print(f"{numero} é um numero primo")
else:
    print(f"{numero} não é um numero primo")