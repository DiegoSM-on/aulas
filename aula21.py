import math

#inicio
vahora = float(input('Qual o valor da sua hora? '))
hrtrabai = float(input('Quantas horas trabalhadas você tem no mês? '))

salaBR = hrtrabai * vahora
FGTS = salaBR * 0.08

print(f'seu salário bruto é: {salaBR}')
print (f'O valor do FGTS é: {FGTS}')

#INSS
if salaBR <= 1412:
    INSS = salaBR = salaBR * 0.925
elif salaBR >= 1412.01 and salaBR <= 2666.68:
    INSS = salaBR = salaBR * 0.91
elif salaBR  >= 2666.69 and salaBR <= 4000.03:
    INSS = salaBR = salaBR * 0.88
else:
    INSS = salaBR = salaBR * 0.86
    

#Imrenda
if salaBR < 2259.20:
    imrenda = print (f'Você não paga imposto de renda!')
if salaBR >= 2259.21 and  salaBR <= 2826.65:
    imerenda = salaBR = salaBR * 0.075
if salaBR >= 2826.66 and salaBR <= 3751.05:
    imrenda = salaBR = salaBR * 0.15
if salaBR >= 3751.06 and salaBR <= 4664.68:
    imrenda = salaBR = salaBR * 0.225
else: 
    imrenda = salaBR * 0.275

#FGTS

salario_liquido = (salaBR - imrenda) - INSS
print(f'O valor descontado do INSS é: {INSS}')
print(f'O valor descontado do Iposto de Renda é: {imrenda}')
print(f'O salário liquido é: {salario_liquido}')

    
