import datetime
pessoa = {}
date = datetime.date.today()
year = int(date.strftime("%Y"))
pessoa['Nome'] = str(input('Digite o seu nome: '))
ano = int(input('Digite seu ano de nascimento: '))
pessoa['Idade'] = year - ano
pessoa['Ctps'] = int(input('Digite sua carteira de trabalho: [0 não tem]'))
if pessoa['Ctps'] == 0:
    print('='*25)
    for c, i in pessoa.items():
        print(f'{c} tem o valor {i}')
else:
    pessoa['Contratação'] = int(input('Qual foi o ano de sua contratação? '))
    pessoa['Salário'] = int(input('Qual o seu salário? '))
    pessoa['Aposentadoria'] = pessoa['Idade'] + (pessoa['Contratação'] + 35) - year
    print('=' * 25)
    for c, i in pessoa.items():
        print(f'{c} tem o valor {i}')