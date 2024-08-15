numero1 = int(input("Digite o primeiro número:"))
operação = input("Digite a operação desejada  (soma = +,subtração = -,multiplicação = *,divisão = /)")
numero2 = int(input("Digite o segundo número:"))
if operação == "+":
    resultado = numero1 + numero2

elif operação == "-":
    resultado = numero1 - numero2

elif operação == "*":
    resultado = numero1 * numero2

elif operação == "/":
    resultado = numero1 / numero2

print(f"{numero1} {operação} {numero2} = {resultado}")