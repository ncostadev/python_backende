number = 22

num_user = int(input('Digite um número positivo: '))

while num_user < number:
    print('\n')
    print('entrada inválida')
    num_user = int(input('Digite outro número positivo: '))

print('\nentrada válida')
