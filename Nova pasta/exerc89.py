lista = list()
listona = list()
tot = 0
while True:
    n = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2)/2
    lista.append(n)
    lista.append(nota1)
    lista.append(nota2)
    lista.append(media)
    listona.append(lista[:])
    lista.clear()
    tot += 1
    resp = str(input('Deseja continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
print('='*50)
print(f'{"BOLETIM":^50}')
print('='*50)
for c in range(0,tot):
    print(f'Aluno {c} {listona[c][0]}        {"Média:":>8} {listona[c][3]}')
while True:
    resp = str(input('Deseja saber a nota de algum aluno separadamente? ')).strip().upper()[0]
    if resp == 'N':
        break
    else:
        esc = int(input('Digite um número correspondente ao aluno: '))
        print(f'As notas de {listona[esc][0]} são {listona[esc][1]} e {listona[esc][2]}.')