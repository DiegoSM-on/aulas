#Crie um jogo de adivinhação:
#Existem 4 palavras em um vetor e o usuário deve informar uma, se ela existir no vetor exiba a mensagem
#acertou.
'''
Dicas:
1 - Crie vetor com qautro palavras
2 - crie uma entrada para receber a dica do usuário
3 - crie uma estrutura de repetição para percorrer o vetor
4 - crie um estrutura condicional comparando o valor lido no momento com o digitado pelo usuário. Se igual
exiba: Você ganhou e coloque um break.
5 - coloque um else dizendo você perdeu. compre mais creditos
'''

vetor: str = ['Diego','Maria','Christina', 'Mateus']
palavra = input('Escreva um nome: ')

for i in vetor:

    if palavra == len[vetor]:
        print('Você acertou')
    else:
        print('Voce errou')




