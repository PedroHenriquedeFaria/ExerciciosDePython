def fatorial(a,b=0):
    """
     Uma função que calcula o fatorial de um número
    :param a: Número a ser calculado
    :param b: Variável de escolha que define a visualização dos cálculos
    :return: Sem retorno
    """
    f = a
    if b == 1:
        for c in range(a-1,1,-1):
            f = f * c
        print(f)
    else:
        for c in range(a-1,1,-1):
            print(f'{f} x {c} = ',end='')
            f = f * c
            print(f)
        print(f)


#Programa principal
n = int(input('Digite um número para saber seu fatorial: '))
esc = int(input('Digite [0] para mostrar os cálculos e [1] para esconder: '))
fatorial(n,esc)