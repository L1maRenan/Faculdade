n = 3
notas=[]
for i in range(n):
    nota = float(input(f"Digite a nota {n}"))
    notas.append(nota)
media = sum(notas)/n

print(f"Sua média é {media:.2f}")