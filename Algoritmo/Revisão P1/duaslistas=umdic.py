paises = [
    "Brazil",
    "Argentina",
    "Canada",
    "Germany",
    "Japan",
    "Australia",
    "India",
    "South Africa",
    "Russia",
    "United Kingdom"
]
capitais = [
    "Brasília",
    "Buenos Aires",
    "Ottawa",
    "Berlin",
    "Tokyo",
    "Canberra",
    "New Delhi",
    "Pretoria",
    "Moscow",
    "London"]

def converter():
    dicionario = {}
    for a,b in zip(paises,capitais):
        dicionario[a] = b
    return dicionario
    
silasmalafaia = converter()
print(silasmalafaia)