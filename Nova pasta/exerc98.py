from time import sleep
def contador(i,f,p):
    print('=' * 30)
    if p == 0:
        p = 1
    if i > f and p > 0:
        p = p * -1
    for c in range(i,f,p):
        print(c,end=' ')
    print(' FIM!')
    print('=' * 30)

#Programa principal
contador(1,11,1)
contador(10,-2,-2)
a = int(input('Digite o início:'))
b = int(input('Digite o final: '))
c = int(input('Digite o passo: '))
contador(a,b,c)