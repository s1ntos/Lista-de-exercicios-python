itens = []

while True:
    print("1 - Adicionar Item")
    print("2 - Remover Item")
    print("3 - Mostrar Lista de Item")
    print("4 - Sair")

    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        item = input("Digite o produto que você deseja adicionar: ")
        itens.append(item)
        print("Item adicionado com sucesso!")
        m = input("deseja adicionar mais? sim ou nao: ")
        if m == "sim":
            item = input("Digite o produto que você deseja adicionar: ")
            itens.append(item)
            print("Item adicionado com sucesso!")
        else:
            print("ok!")

    elif opcao == 2:
        rmv = input("Qual item você deseja remover: ")
        if rmv in itens:
            itens.remove(rmv)
            print("Item removido com sucesso!")

    elif opcao == 3:
        if len(itens) == 0:
            print("Lista vazia!")
        else:
            print(itens)

    elif opcao == 4:
        print("saindo do programa")
        break

    else:
        print("opção invalida!")