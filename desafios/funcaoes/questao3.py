# Função que calcula o fatorial usando FOR.


def fatorial(n):
    resul = 1
    for i in range(1, n + 1):
        resul *= n
    print(resul)

fatorial(5)
