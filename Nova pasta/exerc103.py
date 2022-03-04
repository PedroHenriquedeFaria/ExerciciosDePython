def ficha(nome = 'Alguém',gols = 0):
    print('=====| FICHA TÉCNICA |=====')
    print(f'NOME: {nome}')
    print(f'GOLS: {gols}')


nome = str(input('Digite o nome do jogador: '))
gols = str(input('Quantos gols ele fez? '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols = gols)
else:
    ficha(nome,gols)