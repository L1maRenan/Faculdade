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
# print(livros)

def buscaporcodigo(codigo):
    for i in livros:
        for a in i.values():
            if codigo == a:
                print(i)
                break
        else:
            continue
        break
    else:
        print("Encontramo não man")

def attquantidade(codigo, novaquantidade):
    for i in livros:
        for a in i.values():
            if codigo == a:
                i["Quantidade"] = novaquantidade
                print("Quantidade atualizada!")
                break
        else:
            continue
        break
    else:
        print("Encontramo não man")


def removerlivro(codigo):
    for i in livros:
        for a in i.values():
            if codigo == a:
                livros.remove(i)
                print("Livro removido!")
                break
        else:
            continue
        break
    else:
        print("Encontramo não man")

def listalivros():
    for i in livros:
        print(f"Título: {i['Título']}, Autor: {i['Autor']}, Gênero: {i['Gênero']}, Quantidade: {i['Quantidade']}, Códigoo: {i['Código']}")

# attquantidade(202, 9)
# buscaporcodigo(202)
# removerlivro(101)
# print(livros)
listalivros()