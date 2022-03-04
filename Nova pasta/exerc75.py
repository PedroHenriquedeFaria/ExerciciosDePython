tupla = (int(input('Digite um número: ')),int(input('Digite outro número: ')),
         int(input('Digite outro: ')), int(input(('Digite mais um número: '))))
print(f'Vezes em que o número 9 foi digitado: {tupla.count(9)}')
if 3 in tupla:
    print(f'Primeira posição em que apareceu o número 3: {tupla.index(3)+1}')
else:
    print('Nenhum número 3 foi digitado.')
print(f'Valores pares digitados: ')
for c in range(0,4):
    if tupla[c] % 2 == 0:
        print(tupla[c],end=' ')
