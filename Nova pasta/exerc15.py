km = float(input('Digite a quantidade de Km percorridos: '))
dias = int(input('Por quantos dias ele foi alugado? '))
preco  = 60 * dias + 0.15 * km
print('O preço total a se pagar é de {} reais.'.format(preco))