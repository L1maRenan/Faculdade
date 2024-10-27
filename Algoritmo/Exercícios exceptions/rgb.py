cores = {'vermelho': (255, 0, 0), 'verde': (0, 255, 0), 'azul': 
(0, 0, 255)}

try:
    entrada = input("Digite a cor que desejas saber o valor rgb")
    for a, b in cores.items():
        if entrada == a:
            print(b)

    if entrada not in cores:
        raise ValueError

except ValueError:
    print(f"{entrada} não está disponível na lista")