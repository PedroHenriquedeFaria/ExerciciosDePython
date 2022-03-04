def area(larg, alt):
    a = larg * alt
    print(f'A área do terreno {larg} x {alt} é de {a} m')


#Programa principal
larg = float(input('Qual a largura do terreno? '))
alt = float(input('Qual a altura do terreno? '))
area(larg,alt)