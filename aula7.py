# 1 - Dada a lista [14, 14, 23, 21, 1, 17, 44] crie um programa que conte quantos elementos a lista possui. 
# 2 - Dada a lista [14, 14, 23, 21, 1, 17, 44] crie um programa que conte quantos elementos impares a lista possui. 
# 3 - Dada a lista [14, 14, 23, 21, 1, 17, 44] crie um programa que some todos os valores pares da lista e exiba. 


x: list = [14, 14, 23, 21, 1, 17, 44]
print("A quantidade de elementos é: ", len(x))

n = 0
for i in x:
    if i % 2 != 0:
        n +=1
return n
    else: 
        print("Não existe número impares")

print("Quantidade de número impares na lista", n)
