valuno = ["Alan", "Amalia", "Artur", "Joana", "Mariana"]
vnota1 = [18.9,15,17,20,26.4]
vnota2 = [12.2,29,23,20,28]
vnota3 = [14.1,13,20,19,17.6]
vfrequencia = [50,100,150,120,140]
vsoma = [0,0,0,0,0]
vconceito = [0,0,0,0,0]
i=0
while i <= 4:
    soma = 0
    print("\n", valuno[i])
    soma = (vnota1[i]+vnota2[i]+vnota3[i])
    vsoma[i] = soma
    if (soma >= 60) and (vfrequencia[i]>=150):
        vconceito[i] = "Aprovado"
    elif (soma >= 40) and (vfrequencia[i] >= 80):
        vconceito[i] = "Recuperação"
    else:
        vconceito[i] = "Reprovado"
    print(f"\tSoma das notas = {vsoma[i]}, frequencia = {vfrequencia[i]}, aluno está: {vconceito[i]}")
    i = i+1 