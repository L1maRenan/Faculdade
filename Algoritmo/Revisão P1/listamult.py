lista  = [2,5,4,3,6]
def listamult(numero=1):
    listanova = []
    for i in lista:
       new=  numero*i
       listanova.append(new)
    return listanova

ca = listamult()
print(ca)