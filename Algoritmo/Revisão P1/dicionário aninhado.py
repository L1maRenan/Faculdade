alunos = {
    "Felipe": {
        "Matemática": 8.5,
        "Português": 7.0,
        "Ciências": 9.0
    },
    "Gabriel": {
        "Matemática": 6.5,
        "Português": 8.0,
        "Ciências": 7.5
    },
    "Carla": {
        "Matemática": 9.0,
        "Português": 8.5,
        "Ciências": 9.5
    },
    "Juliana": {
        "Matemática": 7.5,
        "Português": 6.0,
        "Ciências": 8.0
    },
    "Lucas": {
        "Matemática": 8.0,
        "Português": 9.0,
        "Ciências": 7.0
    }
}

def acessar(aluno):
    for a, b in alunos.items():
        if aluno == a:
            print(a,b)

def mudarnota(aluno, materia, nota):
    encontrado = False
    if aluno in alunos:
        if materia in alunos[aluno]:
            alunos[aluno][materia]=nota
            encontrado = True
        else:
            print("Matéria não encontrada.")
    else:
        print("Aluno não encontrado")

mudarnota("Carla", "Português", 6.5)

#print(alunos)
acessar("Carla")