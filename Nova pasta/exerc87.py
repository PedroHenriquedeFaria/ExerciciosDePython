matriz = [[],[],[]]
tot = maior = 0
for c in range(0,3):
    print(f'{c+1}° linha da matriz: ')
    n = int(input('Digite um número: '))
    n1 = int(input('Digite outro número: '))
    n2 = int(input('Digite mais um número: '))
    if n % 2 == 0:
        tot += n
    if n1 % 2 == 0:
        tot += n1
    if n2 % 2 == 0:
        tot += n2
    matriz[c].append(n)
    matriz[c].append(n1)
    matriz[c].append(n2)
print()
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('Total de todos valores pares da matriz: {}'.format(tot))
print(f'Soma dos valores da terceira coluna: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    if matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'Maior valor da segunda linha: {maior}')
