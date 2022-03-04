salario = float(input('Digite seu salário atual: '))
aumento = 15
if salario > 1250:
    aumento = 10
novo = salario + (salario/100)* aumento
print('Seu sálario foi aumentado em \033[35m{}%\033[m.\nValor antigo:'
      ' \033[35m{}\033[m\nValor atual: \033[35m{}\033[m'.format(aumento,salario,novo))