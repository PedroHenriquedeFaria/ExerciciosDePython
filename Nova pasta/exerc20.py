import random
n1 = str(input('Qual o nome do 1° aluno?'))
n2 = str(input('Qual o nome do 2° aluno? '))
n3 = str(input('Qual o nome do 3° aluno? '))
n4 = str(input('Qual o nome do 4° aluno? '))
lista = [n1,n2,n3,n4]
escolha = random.shuffle(lista)
print('A ordem escolhida foi: {}'.format(lista))