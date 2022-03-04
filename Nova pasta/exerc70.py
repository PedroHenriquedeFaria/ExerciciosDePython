total = tot1 = 0
resp = True
while resp == True:
    nome = str(input('Qual o nome do produto? '))
    preço = float(input('Qual o preço do produto? '))
    if total == 0 or preço < menorPr:
        menor = nome
        menorPr = preço
    total += preço
    if preço > 1000:
        tot1 += 1
    escolha = str(input('Deseja continuar? ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'O total gasto na compra foi de {total} reais.')
print(f'Você comprou {tot1} produtos que custam mais de R$ 1000.')
print(f'{menor} é o produto mais barato.')
