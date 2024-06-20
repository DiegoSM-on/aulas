def inicializar_urna(candidatos):
    votos = {candidato: 0 for candidato in candidatos}

    while True:
        print("\nCandidatos disponíveis:")
        for i in range(len(candidatos)):
            print(f"{i + 1} - {candidatos[i]}")

        print("0 - Encerrar votação")

        opcao = input("Escolha uma opção: ")
        
        if opcao.isdigit():  
            opcao = int(opcao)
            if opcao == 0:
                break
            elif 1 <= opcao <= len(candidatos):
                candidato_escolhido = candidatos[opcao - 1]
                if candidato_escolhido in votos:
                    votos[candidato_escolhido] += 1
                    print(f"Voto para {candidato_escolhido} registrado com sucesso!")
                else:
                    print("Candidato não reconhecido. Voto não registrado.")
            else:
                print("Opção inválida. Tente novamente.")
        else:
            print("Opção inválida. Tente novamente.")

    print("\nResultado da votação:")
    for candidato, total_votos in votos.items():
        print(f"{candidato}: {total_votos} votos")

if __name__ == "__main__":
    candidatos = ["Coringa", "Mulher Gato", "Charada","Hera venenosa"]
    inicializar_urna(candidatos)
