def leiaInt(txt):
    n = str(input(txt))
    if n.isnumeric():
        n = int(n)
        return n
    else:
        print('\033[31mErro! Digite um valor numerico!')
        return 'Erro'

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')