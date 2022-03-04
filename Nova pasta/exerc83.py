lista = []
ex = str(input('Digite uma expressão: '))
if ex.count('(') == ex.count(')'):
    print('Expressão válida!')
else:
    print('Expressão inválida!')
