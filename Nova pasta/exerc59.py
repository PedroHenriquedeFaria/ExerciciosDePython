num = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
continuar = True
while continuar == True:
    print("""\033[32m======| MENU |======\033[m  
     
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    """)
    escolha = int(input('Digite uma opção: '))
    if escolha == 1:
        print('A soma de {} com {} é igual a \033[36m{}\033[m.'.format(num,num2,num+num2))
    elif escolha == 2:
        print('O produto de {} por {} é igual a \033[36m{}\033[m.'.format(num, num2, num * num2))
    elif escolha == 3:
        if num == num2:
            print('Os dois números digitados são iguais: \033[36m{}\033[m.'.format(num))
        elif num > num2:
            print('O número {} é maior que {}.'.format(num,num2))
        else:
            print('O número {} é maior que {}.'.format(num2,num))
    elif escolha == 4:
        num = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
    elif escolha == 5:
        continuar = False
    else:
        print('\033[31mOpção inválida!\033[m')
print('Fim do programa.')