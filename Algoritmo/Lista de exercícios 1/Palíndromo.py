palavra = input("Escreva uma palavra:")
if palavra == palavra[::-1]:
    print(f"{palavra} é um palindromo")
else:
    print(f"{palavra} não é um palindromo")