num = 0
soma = 0
numeros = 0
while num != 999:
    num = int(input('Digite um número: [Digite 999 para encerrar o programa]'))
    if num != 999:
        numeros += 1
        soma += num
print('A soma dos {} números digitados é: \033[036m{}'.format(numeros,soma))