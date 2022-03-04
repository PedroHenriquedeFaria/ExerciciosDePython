a1 = int(input('Digite o primeiro termo da progressão: '))
raz = int(input('Digite a razão: '))
i = 1
limite = 11
while i < limite:
    print(a1 + (i - 1) * raz,end=' ')
    i += 1
print('\nFim do programa')
