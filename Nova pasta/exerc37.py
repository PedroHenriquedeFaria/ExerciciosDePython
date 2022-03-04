num = int(input('Digite um número inteiro: '))
escolha = int(input('Digite 1 para converter em binário, 2 para octal e 3 para hexadecimal: '))
if escolha == 1:
    num = bin(num)
elif escolha == 2:
    num = oct(num)
elif escolha == 3:
    num = hex(num)
else:
    print('\033[31mOpção inválida\033[m.')
print('Número convertido: \033[35m{}'.format(num[2:]))
