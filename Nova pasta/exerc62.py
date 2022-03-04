a1 = int(input('Digite o primeiro termo da progressão: '))
raz = int(input('Digite a razão: '))
i = 1
termo = 1
limite = 11
while termo != 0:
    while i < limite:
        print(a1 + (i - 1) * raz,end=' ')
        i += 1
    termo = int(input('\nDeseja mostrar mais alguns termos? [Digite 0 para finalizar] '))
    limite += termo
print('Foram exibidos {} termos.'.format(limite-1))
print('Fim do programa')