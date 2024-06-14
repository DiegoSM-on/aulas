

vetor: str = ['Christina', 'Diego', 'Maria', 'Algyenm']
palavra: str = vetor[2]


while True: 
    
    palavras = input('Escreva uma palavra: ')
    if palavras == len(vetor):
        print('Voce acertou')
        break  
    else:
        print('você errou')
