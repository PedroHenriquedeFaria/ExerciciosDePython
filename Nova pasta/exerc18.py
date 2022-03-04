import math
ang = float(input('Digite o valor do ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('Angulo: {}\nSeno: {:.2f}\nCoseno: {:.2f}\nTangente: {:.2f}'.format(ang,sen,cos,tan))
