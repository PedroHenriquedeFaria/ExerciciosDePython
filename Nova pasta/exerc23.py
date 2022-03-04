num = int(input('Digite um número de 0 a 9999:'))
uni = num//1 % 10
dec = num//10 % 10
cent = num//100 % 10
milh = num//1000 % 10
print('Milhar: {}\nCentena: {}\nDezena: {}\nUidade: {}'.format(milh,cent,dec,uni))
