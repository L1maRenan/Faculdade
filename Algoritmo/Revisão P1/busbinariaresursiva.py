clientes = []
def adicionar_cliente(nome, email, telefone, endereco):
    cliente = [nome, email, telefone, endereco]
    clientes.append(cliente)
    print(f"Clienet {nome} cadastrado com sucesso.")

adicionar_cliente("João Silva", "joao.silva@email.com", "(11) 99999-1234", "Rua das Flores, 123")
adicionar_cliente("Maria Souza", "maria.souza@email.com", "(21) 98888-5678", "Avenida Brasil, 456")
adicionar_cliente("Pedro Oliveira", "pedro.oliveira@email.com", "(31) 97777-9101", "Rua do Sol, 789")
adicionar_cliente("Ana Costa", "ana.costa@email.com", "(41) 96666-2345", "Rua da Lua, 321")
adicionar_cliente("Lucas Pereira", "lucas.pereira@email.com", "(51) 95555-6789", "Avenida Central, 654")
adicionar_cliente("Fernanda Lima", "fernanda.lima@email.com", "(61) 94444-9876", "Rua das Palmeiras, 987")
adicionar_cliente("Carlos Almeida", "carlos.almeida@email.com", "(71) 93333-5432", "Rua do Sol, 432")
adicionar_cliente("Juliana Mendes", "juliana.mendes@email.com", "(81) 92222-8765", "Avenida dos Coqueiros, 876")
adicionar_cliente("Ricardo Santos", "ricardo.santos@email.com", "(91) 91111-2109", "Rua das Acácias, 210")
adicionar_cliente("Bianca Moreira", "bianca.moreira@email.com", "(31) 90000-3210", "Avenida Verde, 321")

def buscabinaria(chave, ini, fim):
    if ini>fim:
        return -1
    meio = (ini+fim) //2
    if meio == chave:
        return clientes[meio]
    elif meio > ini:
        return buscabinaria(chave, ini, meio-1)
    else:
        return buscabinaria(chave, fim, meio+1)
    

a = buscabinaria(3, 0, len(clientes) -1)
print(a)