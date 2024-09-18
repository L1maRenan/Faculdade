def potencia(b,e):
    if e == 0:
        return 1
    return b * potencia(b,e-1)

chapeleta = potencia(3,3)
print(chapeleta)