a1 = int(input('Digite o primeiro termo da progressão: '))
raz = int(input('Digite a razão: '))
for c in range(1,11):
    print(a1 + (c - 1) * raz,end=' ')
