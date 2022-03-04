aluno = {}
aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Média'] = float(input('Digite a média do aluno: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Recuperação'
print('='*30)
print(f'Nome: {aluno["Nome"]}')
print(f'Média: {aluno["Média"]}')
print(f'Situação: {aluno["Situação"]}')
print("="*30)