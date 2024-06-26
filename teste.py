lista_acao: list = []
while True: 
    opcao: str = input("Digite a opcão \n- A para inserir \n - D para deletar \n - S para substituir \n - E para visualizar \n: ")
    if opcao == 'a':
        dado_add: str = input("Informe a ação: ")
        lista_acao.append(dado_add)
        print("Dados inseridos com sucesso!!")
    elif opcao == 'd':
        dado_del: str = input("Informe o nome da ação que deseja excluir: ")
        if dado_del in lista_acao:
            lista_acao.remove(dado_del)
        print("Dados deletados com sucesso!")
    elif opcao == 's': 
        dado_sub: str = input("Informe a ação: ")
        lista_acao[1] = dado_sub
        print("Dados alterados com sucesso!")
    elif opcao == 'e':
        print(lista_acao)
    else:
        print("Programa encerrado")
        