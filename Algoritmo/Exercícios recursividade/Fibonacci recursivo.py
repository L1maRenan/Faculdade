def recfibonacci(n):
    print(n)
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return recfibonacci(n-1) + recfibonacci(n-2)
    

opa = recfibonacci(4)
print(opa)

