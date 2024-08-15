def vogais(texto):
    vogais = "aeiouAEIOU"
    contagem = 0
    i = 0
    while i < len(texto):
        if texto[i] in vogais:
            contagem += 1
        i += 1
    return contagem

texto = input("Digite algo:")
nvogais = vogais(texto)
print(f"Número de vogais: {nvogais}")
