alunosnotas = {
    "Felipe" : 7,
    "Gabriel": 6,
    "Carlinhos": 7,
    "Octávio": 8,
    "Sérgio": 9
    }

def consultar(nome):
    encontrado = False
    for i, seila in alunosnotas.items():
        encontrado = False
        if nome == i:
            print(i,seila)
            encontrado = True
            break
    if encontrado == False:
        print("Encontramo não man")

def mudarnota(nome,nota):
    if nome in alunosnotas:
        alunosnotas[nome] = nota
        print("Nota alterada com sucesso!")
    else:
        print(f"Aluno {nome} não encontrado")

mudarnota("Carlinhos", 9)

consultar("Carlinhos")