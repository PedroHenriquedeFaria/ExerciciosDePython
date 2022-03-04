lista = []
listaP = []
listaI = []
while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        listaP.append(n)
    else:
        listaI.append(n)
    lista.append(n)
    cont = str(input('Deseja adicionar mais um número à lista? ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Lista geral: {lista}')
print(f'Lista dos Pares: {listaP}')
print(f'Lista dos Ímpares: {listaI}')