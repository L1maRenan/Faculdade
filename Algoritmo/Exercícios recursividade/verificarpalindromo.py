def verificar_palindromo(s):
    s = s.replace(" ", "").lower()
    
    if len(s) <= 1:
        return True
    
    if s[0] == s[-1]:
        return verificar_palindromo(s[1:-1])
    
    return False

resultado = verificar_palindromo("arara")
print(resultado)