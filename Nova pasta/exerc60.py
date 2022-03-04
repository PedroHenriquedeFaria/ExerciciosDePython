num = int(input('Digite um número: '))
c = num
while c > 1:
    c = c - 1
    print('{} x {} = '.format(num,c),end='')
    num = num * (c)
    print(num)
print('O fatorial do número digitado é \033[35m{}'.format(num))