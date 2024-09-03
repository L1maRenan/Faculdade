
clientes = []

def adicionar_cliente(nome, email, telefone, endereco):
    cliente = [nome, email, telefone, endereco]
    clientes.append(cliente)
    print(f"Clienet {nome} cadastrado com sucesso.")

def exibir_clientes() :
     for cliente in clientes:
      print(f"Nome: {cliente[0]}, E-mail: {cliente[1]}, Telefone: {cliente[2]}, Endereço: {cliente[3]}")

def buscar_cliente(email):
    for cliente in clientes:
        if cliente[1] == email:
            print(f"Nome: {cliente[0]}, E-mail: {cliente[1]} Telefone: {cliente[2]}, Endereço: {cliente[3]}")


def remover_cliente(email):
    for cliente in clientes:
       if cliente[1] == email:
          clientes.remove(cliente)
          print(f"Cliente correspondente ao E-mail {email} rrrrrrrrrrrrrrrremovido.")
          return
    print("Cliente foi encontrado não man")

# def teste():
#    adicionar_cliente("Little Amostrado", "mr.amostrado@icloud", "216969696969", "Rua dos aparecidos")
#    adicionar_cliente("Jair", "bolsolaço@icloud", "228392892734", "Bangu 2")
#    exibir_clientes()
#    remover_cliente("bolsolaço@icloud")
#    exibir_clientes()
#    buscar_cliente("mr.amostrado@icloud")
def menu():
    while True:
     
     print("1: Exibir clientes.\n2: Buscar clientes por E-mail.\n3: Remor cliente.\n4: Adicionar clientes.\n5: Encerrar programa.")
     escolha = input("Qual opção você deseja acessar?")

     if escolha == "1":
        exibir_clientes()
        
     elif escolha == "2":
        email = input("Digite o E-mail:")
        buscar_cliente(email)

     elif escolha == "3":
        email = input("Digite o E-mail:")
        remover_cliente(email)

     elif escolha == "4":
       nome = input("Digite o nome:")
       email = input("Digite o E-mail:")
       telefone = input("Digite o telefone:")
       endereço = input("Digite o endereço:")
       adicionar_cliente(nome, email, telefone, endereço)

     elif escolha == "5":
        break
     
   #   elif escolha == "6":
   #      teste()
     
     else:
        print("Opção inválida, Tente novamente!")

     


menu()
