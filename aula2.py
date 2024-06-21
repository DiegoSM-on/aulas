#Coleção é um tipo de dado que permite armazenar um conjunto de valores.

#Lista é um tipo de coleção que permite inserir valores e acessar pelo indice.
# Para definir uma lista colocamos []


x: int = [15,12,1,"Diego",2,34]
print(x)
#Acesso pelo indice
print("O valor no indice buscado é:",x[2:]) # ':' serve para separar os elementos da lista
print("A quantidade de elemento na lista é", len(x)) #Verificar o tamanho da lista

#Elementos na lista
for i in x: # Serve para exibir os elementos na lista
    print(i)


'''
Crie uma lista ordenada em ordem crescente
com 10 elementos inteiros. Depois crie uma forma
de verificar se existe um número dentro da lista
'''

