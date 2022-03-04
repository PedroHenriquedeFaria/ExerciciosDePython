velocidade = int(input('Qual a velocidade do veículo? Km/h'))
if velocidade > 80:
    print('Você foi multado.')
    multa = (velocidade - 80) * 7
    print('Valor da multa: {} reais.'.format(multa))