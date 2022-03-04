lista = [int(input('Digite um número: ')),int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite outro número: ')),int(input('Digite mais um número: '))]
maior = menor = 0
posMaior = posMenor = 0
for c in range(0,len(lista)):
    if c == 0:
        maior = menor = lista[c]
    if lista[c] > maior:
        maior = lista[c]
        posMaior = c
    if lista[c] < menor:
        menor = lista[c]
        posMenor = c
print(f'O maior valor digitado foi {maior} na posição {posMaior+1} e o menor foi {menor}, na posição {posMenor+1}.')
