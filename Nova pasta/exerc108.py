from exerc111.utilidadesCeV import moeda

preço = float(input('Digite o preço: \033[33mR$ \033[m'))
print(f'A metade de {moeda.moeda(preço)} é igual a {moeda.moeda(moeda.metade(preço))}')
print(f'O dobro de {moeda.moeda(preço)} é igual a {moeda.moeda(moeda.dobro(preço))}')
print(f'O valor de {moeda.moeda(preço)} aumentado em 10% é {moeda.moeda(moeda.aumentar(preço))}')
print(f'O valor de {moeda.moeda(preço)} diminuído em 13% é {moeda.moeda(moeda.diminuir(preço))}')