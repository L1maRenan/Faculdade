
clientes = {}

def adicionar_cliente(nome, email, telefone, endereco):
    cliente = {"nome": nome, "telefone": telefone, "endereco": endereco}
    clientes[email] = cliente
    print(f"Cliente {nome} cadastrado com sucesso.")

def exibir_clientes():
    for email, cliente in clientes.items():
        print(f"Nome: {cliente['nome']}, E-mail: {email}, Telefone: {cliente['telefone']}, Endereço: {cliente['endereco']}")

def buscar_cliente(email):
    if email in clientes:
        cliente = clientes[email]
        print(f"Nome: {cliente['nome']}, E-mail: {email}, Telefone: {cliente['telefone']}, Endereço: {cliente['endereco']}")
    else:
        print("Cliente não encontrado.")

def remover_cliente(email):
    if email in clientes:
        del clientes[email]
        print(f"Cliente correspondente ao E-mail {email} removido.")
    else:
        print("Cliente não foi encontrado.")

def teste():
   adicionar_cliente("Little Amostrado", "mr.amostrado@icloud", "216969696969", "Rua dos aparecidos")
   adicionar_cliente("Jair", "bolsolaço@icloud", "228392892734", "Bangu 2")
   exibir_clientes()
   remover_cliente("bolsolaço@icloud")
   exibir_clientes()
   buscar_cliente("mr.amostrado@icloud")
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
       
       adicionar_cliente()

     elif escolha == "5":
        break
     
     elif escolha == "6":
        teste()
     
     else:
        print("Opção inválida, Tente novamente!")

     


menu()
