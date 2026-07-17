# Sistema de acesso

user = input('Qual seu nome de usuário? ')
password = input('Qual sua senha? ')

if user == 'admin' and password == '1234':
    print('Bem-vindo!\n')
else:
    print('Usuário ou senha incorretos.\n')
