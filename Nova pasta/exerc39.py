import datetime
ano = int(input('Qual seu ano de nascimento? '))
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = int(date.strftime("%Y"))
idade = year - ano
tempo = 18 - idade
if idade < 18:
    print('Você ainda vai se alistar.\nIdade atual: {}\nTempo que falta para se alistar: {}'.format(idade,tempo))
elif idade == 18:
    print('Está na hora de se alistar.')
else:
    print('Já se passou o tempo de se alistar.\nIdade atual: {}\nTempo que passou o prazo: {}'.format(idade,tempo*-1))