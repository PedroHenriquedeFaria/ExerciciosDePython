maior = menor = média = tot = 0
continuar = True
while continuar == True:
    n = int(input('Digite um valor: '))
    média += n
    tot += 1
    if tot == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    escolha = str(input('Deseja continuar? [S/N]')).strip().upper()
    if escolha == 'N':
        continuar = False
print('A média dos {} números digitados é {:.2f}, o maior número é {} e o menor {}.'.format(tot,média/tot,maior,menor))