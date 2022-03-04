import datetime
date = datetime.date.today()
year = int(date.strftime("%Y"))
def voto(idade):
    if idade >= 18 and idade <= 69:
        return('OBRIGATÓRIO')
    elif idade >= 16 or idade >= 70:
        return('OPCIONAL')
    else:
        return('NEGADO')


#Programa principal
ano = int(input('Digite seu ano de nascimento: '))
idade = year - ano
print(f'Você possui {idade} anos e a situação do seu voto é {voto(idade)}.')