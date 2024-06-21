carrinho_compras = [12,37]

if not carrinho_compras:
       print('o carrinho de compras esta vazio!')
else:
       print ('o carrinho de compras nao esta vazio!')

numero = [1,2,3,4,5]
if all(i > 0 for i in numero):
       print('todos os numeros da lista sao positivos')

#SE e SENAO para lista 
frutas = ('coco','kiwi','morango','uva')

frutaUser = str(input('pesquiser uma fruta:'))

if frutaUser in frutas: 
   print (f'a fruta {frutaUser} existe na lista')
else:
   print (f'a fruta {frutaUser} nao esta na lista') 

   #SE e SENAO
     # != serve para se referir a diferença, ou seja, 0 != 1 (0 é diferente de 1)



numero = [20,30,40,50,60]
if numero:
  maior = max(numero)
  print(f'o maior numero a lista e:{maior}')
else:
    print('a lista esta vazia')

    #duplicadas 
nomes = ['ian','iuri','pedro','jonjon','ian']
if len (nomes)!= len (set(nomes)):
    print ('a elementos duplicados na lista')
else:
    print ('nao ha elementos duplicados na lista')