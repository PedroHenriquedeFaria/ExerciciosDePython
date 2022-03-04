from random import randint
from time import sleep
print("""========| JOKENPÔ |========
[1] Para selecionar PEDRA *
[2] Para selecionar PAPEL #
[3] Para selecionar TESOURA %""")
escolha = int(input('Faça sua escolha: '))
computador = randint(1,3)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
#Caso Pedra
if escolha == 1 and computador == 1:
    print('*  X  *')
    print('\033[36mEmpate!')
elif escolha == 1 and computador == 2:
    print('*  X  #')
    print('\033[35mVitória do Computador!')
elif escolha == 1 and computador == 3:
    print('*  X  %')
    print('\033[34mVitória do Jogador!')
#Caso Papel
elif escolha == 2 and computador == 2:
    print('#  X  #')
    print('\033[36mEmpate!')
elif escolha == 2 and computador == 1:
    print('#  X  *')
    print('\033[34mVitória do Jogador!')
elif escolha == 2 and computador == 3:
    print('#  X  %')
    print('\033[35mVitória do Computador!')
# Caso Tesoura
elif escolha == 3 and computador == 3:
    print('%  X  %')
    print('\033[36mEmpate!')
elif escolha == 3 and computador == 1:
    print('%  X  *')
    print('\033[35mVitória do Computador!')
elif escolha == 3 and computador == 2:
    print('%  X  #')
    print('\033[34mVitória do Jogador!')
else:
    print('\033[31mOpção inválida')
