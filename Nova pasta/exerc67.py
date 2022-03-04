n = 0
while True:
    n = int(input('Digite um número para saber sua tabuada: [Negativo para sair] '))
    if n < 0:
        break
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')