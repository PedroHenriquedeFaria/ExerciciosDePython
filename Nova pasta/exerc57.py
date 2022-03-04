n = 1
while n != 0:
    sexo = str(input('Digite o sexo da pessoa: [M/F]')).strip().upper()
    if sexo == 'M' or sexo == 'F':
        n = 0
    else:
        print('Informe um sexo válido.')
        n = 1
print('Fim')
