frase = str(input('Digite uma frase: ')).strip().upper()
fraseP = frase.split()
junto = ''.join(fraseP)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto,inverso))
if inverso == junto:
    print('É um palíndromo')
else:
    print('A frase digitada não é um palíndromo')