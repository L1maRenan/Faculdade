saldo = float(input("Digite o saldo da conta"))
transferencia = float(input("Digite o valor da transferência"))
try:
    if saldo < transferencia:
        raise ValueError
    
except ValueError:
    print("Valor da transferência excede o saldo.")