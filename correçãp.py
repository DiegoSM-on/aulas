


cesta: str = ['uva',' maça','mamão','pera']
opc: str = input ("Adivinhe uma fruta da cesta: ")
sinal: 0 

for i in cesta:
    if i == opc:
        sinal = 0 
        print('Voce acertou')
        break
    else: 
        sinal = 1 
if sinal == 1:
    print("Valor não encontrado")        
