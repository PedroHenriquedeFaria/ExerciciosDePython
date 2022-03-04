num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 > num2 :
    print('O primeiro valor, \033[032m{}\033[m é maior.'.format(num1))
elif num2 > num1:
    print('O segundo valor, \033[032m{}\033[m é maior.'.format(num2))
else:
    print('Os dois valores digitados são iguais.')
