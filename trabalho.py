def inicializar_urna(candidatos):
    votos = {candidato: 0 for candidato in candidatos}
    total_votos = 0
    print("==="*20)
    while total_votos < 20:
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
                    total_votos += 1
                    print(f"Voto para {candidato_escolhido} registrado com sucesso!")
                    print("==="*20)
                    if total_votos == 20:
                        print("Limite de 20 votos alcançado")
                        break
                else:
                    print("Candidato não reconhecido. Voto não registrado.")
            else:
                print("Opção inválida. escolha um número correspondente ao candidato.")
        else:
            print("Opção inválida. Tente novamente.")

    print("\nResultado da votação:")
    if total_votos > 0:
        for candidato, num_votos in votos.items():
            percentual = (num_votos / total_votos)* 100
            print(f"{candidato}: {percentual:.1f}% dos votos")

if __name__ == "__main__":
    candidatos = ["Coringa", "Mulher Gato", "Charada","Hera venenosa"]
    inicializar_urna(candidatos)
