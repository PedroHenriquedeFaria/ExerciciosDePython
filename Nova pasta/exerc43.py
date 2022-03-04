altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / altura ** 2
if imc < 18.5:
    print('Abaixo do peso')
    print('Imc: {:.2f}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
    print('Imc: {:.2f}'.format(imc))
elif imc >= 25 and imc <= 30:
    print('Sobrepeso')
    print('Imc: {:.2f}'.format(imc))
elif imc <= 40:
    print('Obesidade')
    print('Imc: {:.2f}'.format(imc))
else:
    print('Obesidade mórbida')
    print('Imc: {:.2f}'.format(imc))
