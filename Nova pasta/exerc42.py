l1 = float(input('Digite o primeiro comprimento de reta: '))
l2 = float(input('Digite o segundo comprimento de reta: '))
l3 = float(input('Digite o terceiro comprimento de reta: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print('É possível formar um triângulo.')
    if l1 == l2 and l2 == l3:
        print('Triângulo Equilátero.')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('Triângulo Escaleno.')
    else:
        print('Triângulo Isóceles.')
else:
    print('Não é possível formar um triângulo.')