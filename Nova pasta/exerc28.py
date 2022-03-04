import random
escolhaComp = random.randint(0,5)
escolhaUsuario = int(input('Tente adivinhar o número escolhido de 0 a 5!'))
if(escolhaUsuario == escolhaComp):
    print('Você foi vitorioso!')
else:
    print('Você errou!')
    print('Numero sorteado: {}'.format(escolhaComp))
