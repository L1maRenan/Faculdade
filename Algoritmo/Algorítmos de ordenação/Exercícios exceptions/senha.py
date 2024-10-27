try:
    senha = input("Digite a senha")
    listasenha = list(senha)
    temnumero=False
    for i in listasenha:
        if len(senha)< 8:
            raise NameError
        
    for i in senha:
            if i.isdigit():
                temnumero=True
                break

    if not temnumero:
        raise ValueError
                

except ValueError:
    print("Erro! Senha deve possuir pelo menos um número")

except NameError:
    print("Erro! Senha deve possuir no mínimo oito caracteres.")