preco = float(input('Qual é o preço do produto?'))
print('[1] À vista/cheque: 10% de desconto.')
print('[2] À vista no cartão: 5% de desconto.')
print('[3] Em até 2x no cartão: preço normal.')
print('[4] Em 3x ou mais no cartão: 20% de juros.')
escolha = int(input('Escolha a forma de pagamento: '))
if escolha == 1:
    novo = preco - (preco/100)*10
elif escolha == 2:
    novo = preco - (preco / 100) * 5
elif escolha == 3:
    novo = preco
elif escolha == 4:
    novo = preco + (preco/100)*20
else:
    novo = 0
    print('\033[31mOpção inválida')
print('Valor original: {}\nNovo valor: {}'.format(preco,novo))