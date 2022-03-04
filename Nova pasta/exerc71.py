tot10 = tot1 = tot2 = tot5 = 0
num = int(input('Digite o valor a ser sacado: '))
if num >= 50:
    tot5 = num // 50
    num = num - tot5 * 50
if num >= 20:
    tot2 = num // 20
    num = num - tot2 * 20
if num >= 10:
    tot10 = num // 10
    num = num - tot10 * 10
if num < 10:
    tot1 = num

print(f'Total de notas de 50: {tot5}')
print(f'Total de notas de 20: {tot2}')
print(f'Total de notas de 10: {tot10}')
print(f'Total de notas de 1: {tot1}')
