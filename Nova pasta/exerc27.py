nome = input('Qual é o seu nome completo?').strip()
nomesep = nome.split()
print('Nome completo: {}\nPrimeiro nome: {}'.format(nome,nomesep[0]))
print('Ultimo nome: {}'.format(nomesep[len(nomesep)-1]))
