from random import randint
from time import sleep
lista = list()
listona = list()
cont = 0
n = int(input('Quantos jogos deseja realizar? '))
for c in range(0,n):
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            cont = 0
            break
    listona.append(lista[:])
    lista.clear()
print('  Mega Sena Simulator')
for c in range(0,n):
    print(listona[c])
    sleep(1)