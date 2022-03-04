lista = []
while True:
    n = int(input('Digite um número: '))
    if n in lista:
        print('Número já adicionado à lista.')
    else:
        lista.append(n)
    cont = str(input('Deseja continuar? ')).strip().upper()[0]
    if cont == 'N':
        break
lista.sort()
print(f'Números digitados: {lista}')
