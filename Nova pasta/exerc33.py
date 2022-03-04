num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite outro numero: '))
if num1 > num2 and num2 > num3:
    print('O maior número é {}.'.format(num1))
    print('O menor número é {}.'.format(num3))
if num1 > num3 and num3 > num2:
    print('O maior número é {}.'.format(num1))
    print('O menor número é {}.'.format(num2))
if num2 > num1 and num1 > num3:
    print('O maior núemro é {}.'.format(num2))
    print('O menor número é {}.'.format(num3))
if num2 > num3 and num3 > num1:
    print('O maior núemro é {}.'.format(num2))
    print('O menor número é {}.'.format(num1))
if num3 > num1 and num1 > num2:
    print('O maior núemro é {}.'.format(num3))
    print('O menor número é {}.'.format(num2))
if num3 > num2 and num2 > num1:
    print('O maior núemro é {}.'.format(num3))
    print('O menor número é {}.'.format(num1))
