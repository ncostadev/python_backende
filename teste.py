
class Banco:
    def __init__(self, saldo = 0):
        if saldo < 0:
            print('Saldo negativo')
        self.saldo = saldo
            

    def depositar(self, valor):
        if valor <= 0:
            print('Não pode depositar')
        self.saldo += valor

    def sacar(self, valor):

        if valor <= 0:
            print('Não pode sacar, número negativo')
        elif self.saldo <= 0:
            print('Saldo insuficiente') 
        self.saldo -= valor

p1 = Banco()
p1.depositar(0)
p1.sacar(10)
print(p1.saldo)
