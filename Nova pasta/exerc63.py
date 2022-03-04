n = int(input('Deseja visualizar quantos termos da sequência de Fibonacci? '))
i = 1
num1 = 0
num2 = 1
while i <= n:
    if i == 1:
        print(0,end=' ')
    else:
        print(num2,end=' ')
        num = num1
        num1 = num2
        num2 = num2 + num
    i += 1
    