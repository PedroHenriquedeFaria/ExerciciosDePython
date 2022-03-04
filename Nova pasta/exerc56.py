media = 0
homem = ''
contIdade = 0
contMulher = 0

for c in range(1,5):
    nome = str(input('Digite o nome da {}° pessoa: '.format(c))).strip()
    idade = int(input('Digite a idade da {}° pessoa: '.format(c)))
    sexo = str(input('Digite o sexo da {}° pessoa: '.format(c))).strip().upper()

    if idade > contIdade and sexo == 'MASCULINO':
        contIdade = idade
        homem = nome
    if sexo == 'FEMININO' and idade < 20:
        contMulher += 1

    media += idade

print('A média das idades é de {}.'.format(media/4))
print('O homem mais velho do grupo é {}.'.format(homem))
print('Esse grupo possui {} mulheres.'.format(contMulher))
