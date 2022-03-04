from random import randint
comp = randint(0,10)
tentativas = 0
j = 30
while j != comp:
    j = int(input('Tente adivinhar o número de 0 a 10 escolhido pelo computador!'))
    tentativas += 1
print('Você acertou, parabéns! Foram necessárias \033[32m{}\033[m tentativas!'.format(tentativas))