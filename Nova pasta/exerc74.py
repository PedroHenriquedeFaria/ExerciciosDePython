from random import randint
tupla = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))
print(tupla)
maior = menor = 0
for c in range(0,5):
    if c == 0:
        maior = menor = tupla[c]
    if tupla[c] > maior:
        maior = tupla[c]
    if tupla[c] < menor:
        menor = tupla[c]
print(f'Maior valor: {maior}\nMenor valor: {menor}')