casa = float(input('Digite o valor da casa: '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos deseja pagar? '))
prestacao = casa/(anos*12)
if prestacao > (salario/100)*30:
    print('Emprestimo \033[31mnegado.')
else:
    print('Emprestimo \033[32maprovado.')
    print('\033[mPrestação mensal: \033[33m{}'.format(prestacao))
