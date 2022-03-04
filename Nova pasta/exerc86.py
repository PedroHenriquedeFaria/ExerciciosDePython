matriz = [[],[],[]]
for c in range(0,3):
    print(f'{c+1}° linha da matriz: ')
    n = int(input('Digite um número: '))
    n1 = int(input('Digite outro número: '))
    n2 = int(input('Digite mais um número: '))
    matriz[c].append(n)
    matriz[c].append(n1)
    matriz[c].append(n2)
print()
print(matriz[0])
print(matriz[1])
print(matriz[2])
