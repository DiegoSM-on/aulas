total: int = 0
numero: int = 0

while True: 
    
    numero = int(input("Digite um numero: "))
    if numero < 0:
        break  
    total = total + numero
    print('O total somado é: ', total)
print('O final somado é: ', total)