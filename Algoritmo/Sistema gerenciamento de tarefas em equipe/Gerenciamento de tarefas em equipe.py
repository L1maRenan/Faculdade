lista_tarefas = []

def gerar_id(lista_tarefas):
    if lista_tarefas:
        maior_id = max(tarefa["ID"] for tarefa in lista_tarefas)
        return maior_id + 1
    else:
        return 1

def adicionar_tarefa(lista_tarefas, descricao, status, prioridade):
    tarefa = {
        "ID" : gerar_id(lista_tarefas),
        "Descrição": descricao,
        "Status": status,
        "Prioridade": prioridade
    }
    lista_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso")

adicionar_tarefa(lista_tarefas, "Entregue uma carta na rua das couves", "Pendente", "Média")
adicionar_tarefa(lista_tarefas, "Bate uma laje", "Andamento", "Baixa")

def visualizar_tarefas(lista_tarefas):
    for i in lista_tarefas:
        print (i)

# visualizar_tarefas(lista_tarefas)

def filtrar_tarefas(lista_tarefas, status=None, prioridade=None):
    for i in lista_tarefas:
        if status != None or prioridade != None:
            if status in i:
                print(i)
            elif status in i:
                print(i)
        else:
            visualizar_tarefas(lista_tarefas)
            

def filtrar_tarefas(lista_tarefas, status=None, prioridade=None):
    if status is None and prioridade is None:
        return lista_tarefas
    else:
        return [
            tarefa for tarefa in lista_tarefas
            if (status is None or tarefa["Status"] == status) and 
               (prioridade is None or tarefa["Prioridade"] == prioridade)
        ]
filtro = filtrar_tarefas(lista_tarefas, None, "Baixa")
print(filtro)


# print(lista_tarefas)
