num = int(input('Digite um número: '))
cont = 0
for c in range(1,num):
    if num % c == 0:
       cont += 1
if(cont == 1):
    print('Número \033[35mprimo.')
else:
    print('Número \033[33m"normal"')
