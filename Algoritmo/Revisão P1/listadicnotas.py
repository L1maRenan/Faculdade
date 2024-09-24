alunos = [
    {"João": [8.5, 7.0, 9.0]},
    {"Maria": [6.5, 8.0, 7.5]},
    {"Pedro": [7.0, 6.5, 8.5]},
    {"Ana": [9.5, 8.0, 9.0]},
    {"Lucas": [5.5, 6.0, 7.0]}
]

def media(lista):
    dicalunosmedia = {}
    for a in lista:
        for b, c in a.items():
            a = f"{sum(c)/len(c):.2f}"
            dicalunosmedia[b] = a
    return dicalunosmedia

result = media(alunos)
print(result)