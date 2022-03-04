frase = str(input('Digite uma frase: ')).strip()
print('Quantidade de letras A:',frase.upper().count('A'))
print('Posição que aparece pela primeira vez:',frase.upper().find('A')+1)
print('A ultima aparição da letra A foi:',frase.upper().rfind('A')+1)