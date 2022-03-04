nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
if media < 5:
    print('Média: {}'.format(media))
    print('\033[31mREPROVADO.')
elif media >= 7:
    print('Média: {}'.format(media))
    print('\033[32mAPROVADO.')
else:
    print('Média: {}'.format(media))
    print('\033[36mRECUPERAÇÃO.')
