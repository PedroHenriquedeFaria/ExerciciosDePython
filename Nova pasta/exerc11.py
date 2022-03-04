larg = int(input('Digite a largura da parede: '))
alt = int(input('Digite a altura da parede: '))
area = larg * alt
litros = area / 2
print('A parede possui {} metros de largura e {} metros de altura.\nSua área é de {} m^2 e '
      'serão necessárias {} litros de tinta.'.format(larg,alt,area,litros))