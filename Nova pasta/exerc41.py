import datetime
year = datetime.date.today().year
ano = int(input('Digite seu ano de nascimento:'))
idade = year - ano
print(idade)
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Júnior')
elif idade <=25:
    print('Sênior')
else:
    print('Mestre')