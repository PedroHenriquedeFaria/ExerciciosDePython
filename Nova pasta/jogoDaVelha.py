espacos = [1,2,3,4,5,6,7,8,9]
ocupados = [0,0,0,0,0,0,0,0,0]
rodadas = 0

def jogo():
    for c in range(0, 9):
        print('[', espacos[c], ']', end='')
        if ((c + 1) % 3 == 0):
            print('\n')

jogo()

while rodadas < 9:
    esc =  int(input('Escolha onde vai colocar o "X":'))
    if(ocupados[esc-1]):
        print("Lugar inválido!")
    else:
        ocupados[esc-1] = 1
        espacos[esc-1] = 'X'

    jogo()
    rodadas +=1

    if(rodadas == 9):
        print("Deu velha!")
        break;

    if(espacos[0] == 'X' and espacos[1] == 'X' and espacos[2] == 'X'):
        print("Vitória do jogador X!")
        break;
    if (espacos[3] == 'X' and espacos[4] == 'X' and espacos[5] == 'X'):
        print("Vitória do jogador X!")
        break;
    if (espacos[6] == 'X' and espacos[7] == 'X' and espacos[8] == 'X'):
        print("Vitória do jogador X!")
        break;
    if (espacos[0] == 'X' and espacos[3] == 'X' and espacos[6] == 'X'):
        print("Vitória do jogador X!")
        break;
    if (espacos[1] == 'X' and espacos[4] == 'X' and espacos[7] == 'X'):
        print("Vitória do jogador X!")
        break;
    if (espacos[2] == 'X' and espacos[5] == 'X' and espacos[8] == 'X'):
         print("Vitória do jogador X!")
         break;
    if (espacos[0] == 'X' and espacos[4] == 'X' and espacos[8] == 'X'):
        print("Vitória do jogador X!")
        break;
    if (espacos[2] == 'X' and espacos[4] == 'X' and espacos[6] == 'X'):
         print("Vitória do jogador X!")
         break;


    esc =  int(input('Escolha onde vai colocar o "O":'))
    if(ocupados[esc-1]):
        print("Lugar inválido!")
    else:
        ocupados[esc-1] = 1
        espacos[esc-1] = 'O'

    jogo()
    rodadas +=1
    if (espacos[0] == 'O' and espacos[1] == 'O' and espacos[2] == 'O'):
        print("Vitória do jogador O!")
        break;
    if (espacos[3] == 'O' and espacos[4] == 'O' and espacos[5] == 'O'):
        print("Vitória do jogador O!")
        break;
    if (espacos[6] == 'O' and espacos[7] == 'O' and espacos[8] == 'O'):
        print("Vitória do jogador O!")
        break;
    if (espacos[0] == 'O' and espacos[3] == 'O' and espacos[6] == 'O'):
        print("Vitória do jogador O!")
        break;
    if (espacos[1] == 'O' and espacos[4] == 'O' and espacos[7] == 'O'):
        print("Vitória do jogador O!")
        break;
    if (espacos[2] == 'O' and espacos[5] == 'O' and espacos[8] == 'O'):
        print("Vitória do jogador O!")
        break;
    if (espacos[0] == 'O' and espacos[4] == 'O' and espacos[8] == 'O'):
        print("Vitória do jogador O!")
        break;
    if (espacos[2] == 'O' and espacos[4] == 'O' and espacos[6] == 'O'):
        print("Vitória do jogador O!")
        break;
