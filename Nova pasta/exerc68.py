from random import randint
vitorias = 0
while True:
    jogador = str(input('Escolha Par [P] ou Impar [I]: ')).strip().upper()[0]
    n = int(input('Quantos dedos irá mostrar?'))
    nc = randint(0,10)
    print(f'Seu adversario mostrou {nc} dedos.')
    if (n+nc)%2 == 0 and jogador == 'P':
        print('Vitória!')
        vitorias += 1
    elif (n+nc)%2 == 0 and jogador == 'I':
        print('Derrota!')
        break
    elif (n+nc)%2 != 0 and jogador == 'P':
        print('Derrota!')
        break
    elif (n + nc) % 2 != 0 and jogador == 'I':
        print('Vitória!')
        vitorias += 1
print(f'Você obteve {vitorias} vitorias, parabéns!')
