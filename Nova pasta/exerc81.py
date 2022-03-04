tot = 0
lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    tot += 1
    cont = str(input('Deseja adicionar mais um número à lista? ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Foram digitados {tot} números.')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print(f'Foram digitados {lista.count(5)} números 5.')
else:
    print('Não foi digitado nenhum valor 5.')