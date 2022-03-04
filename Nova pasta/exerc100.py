from random import randint
números = list()
def sorteia():
    for c in range(0,5):
        números.append(randint(0,10))
    print(f'Números sorteados: {números}')


def somaPar():
    soma = 0
    for c in range(0,5):
        if números[c] % 2 == 0:
            soma += números[c]
    print(f'A soma dos valores pares sorteados é {soma}.')


#Programa principal
sorteia()
somaPar()