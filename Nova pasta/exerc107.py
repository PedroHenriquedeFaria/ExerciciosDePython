from exerc111.utilidadesCeV import moeda

preço = float(input('Digite o preço: \033[33mR$ \033[m'))
print(f'A metade de {preço} é igual a R$ {moeda.metade(preço)}')
print(f'O dobro de {preço} é igual a R$ {moeda.dobro(preço)}')
print(f'O valor de {preço} aumentado em 10% é R$ {moeda.aumentar(preço)}')
print(f'O valor de {preço} diminuído em 13% é R$ {moeda.diminuir(preço)}')