from exerc111.utilidadesCeV import moeda

preço = float(input('Digite o preço: \033[33mR$ \033[m'))
print(f'A metade de {moeda.moeda(preço)} é igual a {moeda.metade(preço, True)}')
print(f'O dobro de {moeda.moeda(preço)} é igual a {moeda.dobro(preço, True)}')
print(f'O valor de {moeda.moeda(preço)} aumentado em 10% é {moeda.aumentar(preço, True)}')
print(f'O valor de {moeda.moeda(preço)} diminuído em 13% é {moeda.diminuir(preço, True)}')