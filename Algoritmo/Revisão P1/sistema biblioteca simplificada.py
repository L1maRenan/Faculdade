livros = []

livros = []
def add_livro(titulo, autor, genero, quantidade, codigo):
    livro = {
        "Título": titulo,
        "Autor": autor,
        "Gênero": genero,
        "Quantidade": quantidade,
        "Código": codigo
    }
    livros.append(livro)

add_livro("A","B", "C", 4, 101)
add_livro("N","Y", "P", 7, 202)

def buscarporcodigo(codigo):
    for i in livros:
        if i["Código"] == codigo:
            print(i)
            break
    else:
        print("Tem não manolo")

def atualizarestoque(codigo, estoque):
    for i in livros:
        if i["Código"] == codigo:
            i["Quantidade"] = estoque
            break
        else:
            print("Tem esse livro não.")

def removerlivro(código):
    for i in livros:
        if i["Código"] == código:
            livros.remove(i)
            break
    else:
        print("Livro não encontrado")

def exibirlivros():
    if not livros:
        print("Nenhum lirvo cadastrado")
    for i in livros:
        print(f"Título: {i['Título']}, Autor: {i['Autor']}, Gênero: {i['Gênero']}, Quantidade: {i['Quantidade']}, Código: {i['Código']}")

buscarporcodigo(111)
atualizarestoque(101, 9)
removerlivro(202)
removerlivro(101)
exibirlivros()
# print(livros)