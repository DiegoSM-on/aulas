

acoes_lista: list = []

while True: 
    print("\n1 - Adicionar ação")
    print("2 - Remover ação")
    print("3 - alterar as ações")
    print("4 - Excluir a lista")
    print("5 - Ler a lista")
    print("6 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1': 
        nome_acao = input("Digite o nome da ação: ")
        acoes_lista.append(nome_acao)
    elif opcao == '2':
        for i in acoes_lista:
            print("Açoes", i)
        nome_acao = (input("Digite a ação a ser removida: "))
        acoes_lista.remove(nome_acao)
    elif opcao == '3': 
        nome_acao = (input("Digite a ação a ser alterada: ",[]))
        nome_acao = input("Digite a ação que deseja adicionar")
    elif opcao == '4':
        acoes_lista.clear()
    elif opcao == '5': 
        for i in acoes_lista:
            print(acoes_lista)
    elif opcao == '6': 
        break
print(acoes_lista)
        





