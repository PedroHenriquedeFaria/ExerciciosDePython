tupla = ('Borracha',1.00,'Caneta',2.50,'Caderno',5.00,'Corretivo',3.50,'Lápis',2.00,'Mochila',80,
         'Régua',8.0,'Estojo',50)
print(f'{"LISTAGEM DE PREÇOS":^30}')
for c in range (0,16,2):
    print(f'{tupla[c]:.<25} R${tupla[c+1]:>}')