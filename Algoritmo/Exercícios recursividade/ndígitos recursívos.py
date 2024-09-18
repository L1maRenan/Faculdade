def recdigitos(n):
    if n < 10:
        return 1 
    return 1 + recdigitos(n // 10)

# def contar_digitos(numero):
#     # # Tratamento para números negativos
#     # if numero < 0:
#     #     numero = -numero
    
#     # Caso base: se o número é menor que 10, ele tem um único dígito
#     if numero < 10:
#         return 1
#     else:
#         # Caso recursivo: divida o número por 10 e adicione 1
#         return 1 + contar_digitos(numero // 10)

# opa= contar_digitos(100)
opa = recdigitos(12345)
print(opa)