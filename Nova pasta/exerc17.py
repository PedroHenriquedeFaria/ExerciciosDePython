from math import sqrt
cato = float(input('Digite o valor do cateto oposto: '))
cata = float(input('Digite o valor do cateto adjacente: '))
hipo = sqrt(cato ** 2 + cata ** 2)
print('Cateto oposto: {}\nCateto adjacente: {}\nHipotenusa: {:.2f}'.format(cato,cata,hipo))