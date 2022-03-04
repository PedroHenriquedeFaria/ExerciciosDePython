pessoa = {}
lista = []
listaM = []
listaI = []
media = 0
quant = int(input('Quantas pessoas irá cadastrar? '))
for c in range(0,quant):
    pessoa['Nome'] = str(input(f'Digite o nome da {c+1}ª pessoa: '))
    pessoa['Sexo'] = str(input(f'Digite o sexo da {c+1}ª pessoa: ')).strip().upper()[0]
    pessoa['Idade'] = int(input(f'Digite a idade da {c+1}ª pessoa: '))
    if pessoa['Sexo'] == 'F':
        listaM.append(pessoa.copy())
    media += pessoa['Idade']
    lista.append(pessoa.copy())
    pessoa.clear()
print(f'Foram cadastradas {quant} pessoas.')
print(f'A média das idades foi igual a {media/quant:.2f}')
print(f'Lista das mulheres: {listaM}')
print(f'Lista das pessoas com idade acima da média:')
for c in lista:
    if lista['Idade'] >= media/quant:
        print(lista[c]['Nome'])