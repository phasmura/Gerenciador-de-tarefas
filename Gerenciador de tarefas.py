tarefas = []

print("GERENCIADOR DE TAREFAS")
print("Comandos disponíveis:")

print("1-Adicionar nova tarefa.")
print("2-Listar tarefas existentes.")
print("3-Marcar tarefa como concluida.")
print("4-Editar tarefa.")
print("5-Remover tarefa.")
print("6-Sair do sistema.")


while True:
    comando = input("\nDigite um comando: ")

    if comando == "1":
        titulo = input("Digite o título da tarefa: ")
        tarefa = {"titulo": titulo, "concluida": False}
        tarefas.append(tarefa)
        print("Tarefa adicionada!")

    elif comando == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nLISTA DE TAREFAS:")
            for i in range(len(tarefas)):
                status = "✓" if tarefas[i]["concluida"] else " "
                print(f"{i} - [{status}] {tarefas[i]['titulo']}")

    elif comando == "3":
        indice = int(input("Digite o número da tarefa: "))
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Índice inválido!")

    elif comando == "4":
        indice = int(input("Digite o número da tarefa: "))
        if 0 <= indice < len(tarefas):
            novo_titulo = input("Novo título: ")
            tarefas[indice]["titulo"] = novo_titulo
            print("Tarefa atualizada!")
        else:
            print("Índice inválido!")  

    elif comando == "5":
        indice = int(input("Digite o número da tarefa: "))
        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            print("Tarefa removida!")
        else:
            print("Índice inválido!")

    elif comando == "6":
        print("Saindo...")
        break

    else:
        print("Comando não reconhecido.")