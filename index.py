import getpass
import time
from colorama import Fore, init
import getpass
import pwinput



init(autoreset=True)
print('')
print('')
print('Bem vindo ao sistema.')
print('')
print('')
print('')
time.sleep(1)


print('Carregando')

for a in range(30):
    print('...', end='')
    time.sleep(0.2)
print('...')
print('')
print('')

while True:
    campo_login = input('Usuário: ')
    campo_login = campo_login.lower()
    campo_senha = pwinput.pwinput('Senha: ', '⬤')

    if campo_login == 'vinisaid' and campo_senha == '876':
        break
    else:
        print(Fore.RED + 'Dados inválidos')
        time.sleep(1)
        print('')
        print('')


result = 2
while result != 1:
    print(' ')
    print(' ')
    print('PÁGINA INICIAL')
    print('______________________________________')
    print(' ')
    print(' ')
    print(' ')
    print('1 = SIM')
    print('2 = NÃO')
    print(' ')
    print(' ')
    print(' ')
    print('0')

    result = int(input('DESEJA SAIR NO SISTEMA OPERACIONAL?'))


print('')
print('')
print('')
print('')
print('Desligando')

for a in range(30):
    print('...', end='')
    time.sleep(0.2)
print('...')
print('')
print('')







