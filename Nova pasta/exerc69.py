resp = True
a = b = c = 0
while resp == True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
    if idade >= 18:
        a += 1
    if sexo == 'M':
        b += 1
    if sexo == 'F' and idade < 20:
        c += 1
    escolha = str(input('Deseja continuar?')).strip().upper()[0]
    if escolha == 'N':
        resp = False
print(f'Pessoas com mais de 18 anos: {a}')
print(f'Homens cadastrados: {b}')
print(f'Mulheres com menos de 20 anos: {c}')
