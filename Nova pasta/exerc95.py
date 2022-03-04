jogador = {}
jogadores = []
tot = esc = 0
quantJ = int(input('Quantos jogadores serão adicionados? '))
for j in range(0,quantJ):
    jogador['Nome'] = str(input(f'Digite o nome do {j+1}° jogador: '))
    quant = int(input('Quantas partidas foram jogadas? '))
    jogador['Partidas'] = quant
    for c in range(0,quant):
        jogador[f'Jogo{c+1}'] = int(input(f'Quantos gols foram feitos no {c+1} jogo? '))
        tot += jogador[f'Jogo{c+1}']
    print(f'O jogador {jogador["Nome"]} realizou um total de {tot} gols em {quant} partidas.')
    jogador['Total'] = tot
    tot = 0
    for c in range(0,quant):
        print(f'Gols na {c+1}ª partida: {jogador[f"Jogo{c+1}"]}')
    jogadores.append(jogador.copy())
    jogador.clear()
print('=-'*29)
print('JOGADORES               GOLS                 TOTAL')
for c in range(0,quantJ):
    print(f'\n{jogadores[c]["Nome"]}',end= ' '*15)
    for i in range(0,jogadores[c]['Partidas']):
        print(f'[ {jogadores[c][f"Jogo{i+1}"]}',end=']')
    print(' '*15,f'{jogadores[c]["Total"]}')

print('=-'*29)
while esc != 999:
    esc = int(input('Deseja saber os dados de algum jogador?[999 para sair]'))
    print(f"=====| Levantamento do Jogador {jogadores[esc]['Nome']} |=====")
    for i in range(0,jogadores[esc]['Partidas']):
        print(f'Gols na {i+1}ª partida: {jogadores[esc][f"Jogo{i+1}"]}')