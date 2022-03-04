from random import randint
bibli = {}
listN = []
listR = []
maior = maiorn = 0
for c in range(0,4):
    n = str(input(f'Qual o nome do {c+1}° jogador?'))
    r = randint(1,6)
    listN.append(n)
    listR.append(r)
bibli['Nomes'] = listN
bibli['Resultados'] = listR
for c in range(0,4):
    print(f'{bibli["Nomes"][c]} teve o resultado {bibli["Resultados"][c]}')
for c in range(0,4):
    if c == 0:
        maior = bibli['Resultados'][c]
    elif bibli['Resultados'][c] > maior:
        maior = bibli['Resultados'][c]
        maiorn = c
print(f'O vencedor foi {bibli["Nomes"][maiorn]} com o resultado {maior}.')