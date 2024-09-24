def dias(seg,ter,qua,qui,sex):
    diasehoras = {
        "Segunda" : seg,
        "Terça": ter,
        "Quarta": qua,
        "Quinta": qui,
        "Sexta": sex
    }
    return sum(diasehoras.values())

abadiadewhestviell = dias(8, 5, 6, 10, 9)
print(abadiadewhestviell)
