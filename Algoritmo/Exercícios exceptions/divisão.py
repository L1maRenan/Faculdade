try:
   numero1 = int(input("Digite o primeiro número"))
   numero2 = int(input("Digite o segundo número"))
   divisão = numero1/numero2
   print(divisão)
   
except ZeroDivisionError:
    print("Erro! Impossível dividir por zero.")
except ValueError:
    print("Erro! Valor inválido.")
