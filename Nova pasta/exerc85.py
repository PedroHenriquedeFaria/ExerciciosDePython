lista = list()
listaP = list()
listaI = list()
for c in range(0,7):
    n = int(input(f'Digite o {c+1}° número: '))
    if n % 2 == 0:
        listaP.append(n)
    else:
        listaI.append(n)
lista.append(listaP)
lista.append(listaI)
lista[0].sort()
lista[1].sort()
print(f'Valores pares digitados: {lista[0]}')
print(f'Valores impares digitados: {lista[1]}')
