galera = list()
pessoas = list()
tantas = 0
maior = menor = 0
while True:
    pessoas.append(str(input('Digite o nome da pessoa: ')))
    pessoas.append(float(input('Digite o peso da pessoa: ')))
    galera.append(pessoas[:])
    pessoas.clear()
    tantas += 1
    resp = str(input('Deseja inserir mais pessoas? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Foram cadastradas {tantas} pessoas.')
for p in range(0,len(galera)):
    if p == 0:
        maior = galera[p][1]
        menor = galera[p][1]
    if galera[p][1] > maior:
        maior = galera[p][1]
    if galera[p][1] < menor:
        menor = galera[p][1]
print(f'O maior peso foi de {maior} KG de ',end='')
for p in galera:
    if p[1] == maior:
        print(p[0],end=' ')
print(f'\nO menor peso foi de {menor} KG de ',end='')
for p in galera:
    if p[1] == menor:
        print(p[0],end=' ')
