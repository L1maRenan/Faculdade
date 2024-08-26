
clientes = []

def adicionar_cliente(nome, email, telefone, endereco):
    cliente = [nome, email, telefone, endereco]
    clientes.append(cliente)

def exibir_clientes() :
     for cliente in clientes:
      print(f"Nome: {cliente[0]}, E-mail: {cliente[1]} Telefone: {cliente[2]}, Endereço: {cliente[3]}")

def buscar_cliente(email):
    for cliente in clientes:
        if cliente[1] == email:
            print(f"Nome: {cliente[0]}, E-mail: {cliente[1]} Telefone: {cliente[2]}, Endereço: {cliente[3]}")


def remover_cliente(email):
    global clientes
    for cliente in clientes:
       if cliente[1] == email:
          clientes.remove(cliente)
    
def menu():
    while True:
     
     print("1: Exibir clientes.\n2: Buscar clientes por E-mail.\n3: Remor cliente.\n4: Adicionar clientes.\n5: Encerrar programa.")
     escolha = input("Qual opção você deseja acessar?")

     if escolha == "1":
        exibir_clientes()
        
     elif escolha == "2":
        email = input("Digite o E-mail do cliente:")
        buscar_cliente(email)

     elif escolha == "3":
        email = input("Digite o E-mail do cliente:")
        remover_cliente(email)

     elif escolha == "4":
        nome = input("Digite o nome do cliente:")
        email = input("Digite o E-mail do cliente:")
        telefone = input("Digite o telefone do cliente:")
        endereço = input("Digite o endereço do cliente:")
        adicionar_cliente(nome, email, telefone, endereço)
        print("Cliente adicionado com sucesso!")

     elif escolha == "5":
        break
     
     else:
        print("Opção inválida, Tente novamente!")

     


menu()



