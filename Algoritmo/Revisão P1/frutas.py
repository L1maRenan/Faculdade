frutas = []
fruta = input("Digite cinco nomes de fruta, semparando-as por virgula")
frutas.extend(fruta)
frutaverificar = input("Digite a fruta que você deseja saber se está na lista")
if frutaverificar in frutas:
    print(f"{frutaverificar} está na lista.")
else:
    print(f"{frutaverificar} está na lista.")
