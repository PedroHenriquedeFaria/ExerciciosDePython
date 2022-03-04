from datetime import date
year = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    nasc = int(input(('Digite o ano do nascimento da {}° pessoa: '.format(c))))
    ano = year - nasc
    if ano < 18:
        menor += 1
    else:
        maior += 1
print('\033[35m{}\033[m pessoas atingiram a maioridade e \033[031m{}\033[m ainda são menores.'.format(maior,menor))