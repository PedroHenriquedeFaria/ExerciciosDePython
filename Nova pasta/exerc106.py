fun = 'a'
while fun != 'fim':
    print('\033[36m~'*30)
    print('SISTEMA DE AJUDA PyHELP')
    print('~'*30)
    fun = str(input('Função ou biblioteca -> ')).strip().lower()
    print('\033[31m')
    help(fun)