soma = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma += c
print('Soma dos números ímpares múltiplos de 3 entre 1 e 500: \033[35m{}'.format(soma))
