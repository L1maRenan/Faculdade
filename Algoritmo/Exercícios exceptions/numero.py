numero = int(input("Digite um número"))

try:
    if numero > 10:
        print("Número válido")
    else:
        print("Programa executado com sucesso!")

finally:
    print("Programa encerrado")