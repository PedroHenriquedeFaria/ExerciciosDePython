tupla = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze'
         ,'Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    num = int(input('Digite um número de 0 a 20:'))
    if num >= 0 and num <= 20:
        print(tupla[num])
    else:
        print('Digite um valor válido.')
    continuar = str(input('Deseja continuar?')).strip().upper()[0]
    if continuar == 'N':
        break