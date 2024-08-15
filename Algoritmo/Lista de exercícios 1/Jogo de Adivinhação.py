import random
numero = random.randint(1, 101)
tentativa = int(input("Tente acertar o unimero em que estou pensando:"))
while tentativa != numero:
    if tentativa > numero:
        tentativa = int(input(f"Respota errada, o meu número é menor que {tentativa}, tente novamente:"))

    elif tentativa < numero:
        tentativa = int(input(f"Respota errada, o meu número é maior que {tentativa}, tente novamente:"))

print(f"Correto, o meu número é {numero}")