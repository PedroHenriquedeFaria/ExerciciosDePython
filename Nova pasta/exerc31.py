distancia = int(input('Qual a distância da viagem?'))
if distancia <= 200:
    valor = distancia * 0.5
    print('O valor da passagem é de {} reais.'.format(valor))
else:
    valor = distancia * 0.45
    print('O valor da passagem é de {} reais.'.format(valor))
