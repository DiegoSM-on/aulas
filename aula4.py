
x: list = [0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
data: int = int(input("\n Digite um número: "))


#for i in range(len(lista)):
for i in x:
    if i == data:
        print("O número escolido bateu")
        break
    else: 
        print('você errou')

