def maior(*num):
    for c in range(0,len(num)):
        if c == 0:
            maiorA = num[c]
        if num[c] > maiorA:
            maiorA = num[c]
    print(f'Foram informados {len(num)} valores e o maior deles foi {maiorA}.')


#Programa principal
maior(5,2,4,2,6)
