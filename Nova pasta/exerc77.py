tupla = ('playlist','Jasmim','sonhos','dia','alem','girassol','noite','sol','ver','nao'
         ,'dormir','acordado','vida','caminho','saida','girar')
for c in range(0,len(tupla)):
    print(f'\nVogais em {tupla[c]}:')
    if 'a' in tupla[c] or 'A' in tupla[c]:
        print('a',end=' ')
    if 'e' in tupla[c] or 'E' in tupla[c]:
        print('e', end=' ')
    if 'i' in tupla[c] or 'I' in tupla[c]:
        print('i',end=' ')
    if 'o' in tupla[c] or 'O' in tupla[c]:
        print('o',end=' ')
    if 'u' in tupla[c] or 'U' in tupla[c]:
        print('u',end=' ')