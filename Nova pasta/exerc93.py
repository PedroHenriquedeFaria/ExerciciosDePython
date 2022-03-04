jogador = {}
tot = 0
jogador['Nome'] = str(input('Digite o nome do jogador: '))
quant = int(input('Quantas partidas foram jogadas? '))
for c in range(0,quant):
    jogador[f'Jogo{c+1}'] = int(input(f'Quantos gols foram feitos no {c+1} jogo? '))
    tot += jogador[f'Jogo{c+1}']
print(f'O jogador {jogador["Nome"]} realizou um total de {tot} gols em {quant} partidas.')
for c in range(0,quant):
    print(f'Gols na {c+1}ª partida: {jogador[f"Jogo{c+1}"]}')
