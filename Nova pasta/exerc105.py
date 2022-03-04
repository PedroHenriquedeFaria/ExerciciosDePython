def notas(*num,sit = False):
    """
     Esse função recebe a nota de vários alunos e as armazena em uma biblioteca
    :param num: Notas dos alunos
    :param sit: Situação opcional para verificar o desempenho geral da turma
    :return: Retorna a biblioteca contendo a maior e menor nota, média, etc
    """
    bibli = {}
    maior = media = menor = 0
    bibli['Total'] = len(num)
    for c in range(0,len(num)):
        if c == 0:
            maior = num[c]
            menor = num[c]
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
        media += num[c]
    bibli['Maior'] = maior
    bibli['Menor'] = menor
    bibli['Média'] = media/len(num)
    if sit == True:
       if bibli['Média'] >= 7:
           bibli['Situação'] = 'Boa'
       elif bibli['Média'] >= 5:
           bibli['Situação'] = 'Razoavel'
       else:
           bibli['Situação'] = 'Ruim'

    return bibli


resp = notas(5.5,2.5,1.5,sit = True)
print(resp)
help(notas)